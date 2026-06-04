"""
Monte Carlo tournament simulator for WC 2026.

Runs N full tournament simulations and tallies:
  - Probability each team wins the tournament
  - Probability of reaching each knockout round
  - Expected group-stage points and goal difference
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any

import numpy as np

from src.data.teams import TEAMS, all_groups, get_group_teams
from src.data.fixtures import group_fixtures, THIRD_PLACE_SLOTS
from src.engine.predictor import simulate_match

_ROUND_KEYS = ["r32", "r16", "qf", "sf", "final", "winner"]


def _simulate_group_stage(rng: np.random.Generator) -> dict[str, dict]:
    """
    Simulate full group stage. Returns standings dict keyed by team code:
      {points, gd, gf, ga, wins, draws, losses, group}
    """
    standings: dict[str, dict] = {}
    for code in TEAMS:
        standings[code] = {"points": 0, "gd": 0, "gf": 0, "ga": 0,
                            "wins": 0, "draws": 0, "losses": 0,
                            "group": TEAMS[code]["group"]}

    for group in all_groups():
        for a, b in group_fixtures(group):
            ga, gb, pen = simulate_match(a, b, knockout=False, rng=rng)
            standings[a]["gf"] += ga
            standings[a]["ga"] += gb
            standings[a]["gd"] += ga - gb
            standings[b]["gf"] += gb
            standings[b]["ga"] += ga
            standings[b]["gd"] += gb - ga
            if ga > gb:
                standings[a]["points"] += 3
                standings[a]["wins"] += 1
                standings[b]["losses"] += 1
            elif ga < gb:
                standings[b]["points"] += 3
                standings[b]["wins"] += 1
                standings[a]["losses"] += 1
            else:
                standings[a]["points"] += 1
                standings[a]["draws"] += 1
                standings[b]["points"] += 1
                standings[b]["draws"] += 1

    return standings


def _group_ranking_key(s: dict) -> tuple:
    """Sort key: points desc → gd desc → gf desc."""
    return (-s["points"], -s["gd"], -s["gf"])


def _advancing_teams(standings: dict[str, dict]) -> list[str]:
    """
    Determine 32 teams advancing from group stage.
    Top 2 from each of 12 groups = 24 teams.
    Best 8 third-place teams = 8 more → 32 total.
    """
    top2: list[str] = []
    third_place: list[str] = []

    for group in all_groups():
        group_teams = get_group_teams(group)
        ranked = sorted(group_teams, key=lambda c: _group_ranking_key(standings[c]))
        top2.extend(ranked[:2])
        third_place.append(ranked[2])

    # Best 8 third-place teams by points → gd → gf
    third_place.sort(key=lambda c: _group_ranking_key(standings[c]))
    top2.extend(third_place[:THIRD_PLACE_SLOTS])
    return top2


def _simulate_knockout_round(teams: list[str], rng: np.random.Generator) -> list[str]:
    """Simulate one knockout round. Returns list of winners."""
    winners = []
    for i in range(0, len(teams), 2):
        a, b = teams[i], teams[i + 1]
        ga, gb, pen = simulate_match(a, b, knockout=True, rng=rng)
        if pen:
            winners.append(pen)
        elif ga > gb:
            winners.append(a)
        else:
            winners.append(b)
    return winners


def run_simulation(n: int = 100_000, seed: int | None = None) -> dict[str, Any]:
    """
    Run N full tournament simulations.

    Returns
    -------
    dict with:
      "probabilities": {team_code: {round_key: probability, ...}}
      "group_avg": {team_code: {points, gd, gf, ...}}   (averages across sims)
      "n_simulations": int
    """
    rng = np.random.default_rng(seed)

    counters: dict[str, dict[str, int]] = {
        code: {k: 0 for k in _ROUND_KEYS} for code in TEAMS
    }
    group_totals: dict[str, dict[str, float]] = {
        code: {"points": 0.0, "gd": 0.0, "gf": 0.0, "ga": 0.0}
        for code in TEAMS
    }

    for _ in range(n):
        standings = _simulate_group_stage(rng)

        # Accumulate group-stage totals
        for code, s in standings.items():
            for field in ("points", "gd", "gf", "ga"):
                group_totals[code][field] += s[field]

        # Knockout stage
        advancing = _advancing_teams(standings)

        # Shuffle advancing teams into a bracket (random seeding for simplicity)
        rng.shuffle(advancing)

        r32_winners = _simulate_knockout_round(advancing, rng)
        for t in advancing:
            counters[t]["r32"] += 1
        r16_winners = _simulate_knockout_round(r32_winners, rng)
        for t in r32_winners:
            counters[t]["r16"] += 1
        qf_winners = _simulate_knockout_round(r16_winners, rng)
        for t in r16_winners:
            counters[t]["qf"] += 1
        sf_winners = _simulate_knockout_round(qf_winners, rng)
        for t in qf_winners:
            counters[t]["sf"] += 1
        final_winner = _simulate_knockout_round(sf_winners, rng)
        for t in sf_winners:
            counters[t]["final"] += 1
        counters[final_winner[0]]["winner"] += 1

    probabilities: dict[str, dict[str, float]] = {}
    for code in TEAMS:
        probabilities[code] = {k: counters[code][k] / n for k in _ROUND_KEYS}

    group_avg: dict[str, dict[str, float]] = {}
    for code in TEAMS:
        group_avg[code] = {k: v / n for k, v in group_totals[code].items()}

    return {
        "probabilities": probabilities,
        "group_avg": group_avg,
        "n_simulations": n,
    }
