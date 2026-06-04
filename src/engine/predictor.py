"""
Match outcome predictor using Poisson-distributed goal scoring.

Composite team strength:
  40% Elo rating  |  25% recent form  |  20% squad quality  |  15% WC experience
"""

from __future__ import annotations

import numpy as np

from src.data.teams import TEAMS, elo_win_probability
from src.data.players import squad_avg_rating, squad_form_score, key_player_boost

_RNG = np.random.default_rng()

# Average goals per team per match in major tournaments (slightly below open-play avg)
BASE_GOAL_RATE = 1.18


def _composite_strength(team_code: str) -> float:
    """
    Returns a composite strength multiplier centred at 1.0 (average tournament team).
    Used to scale expected goals up or down.
    """
    t = TEAMS[team_code]
    elo_norm = t["elo"] / 1800.0                          # 1800 ≈ average qualifier
    form_norm = t["form"] / 10.0
    squad_norm = squad_avg_rating(team_code) / 80.0        # 80 ≈ average squad
    wc_norm = t["wc_experience"] / 10.0

    strength = (
        0.40 * elo_norm
        + 0.25 * form_norm
        + 0.20 * squad_norm
        + 0.15 * wc_norm
    )
    # Multiply by key-player boost (±10%)
    return strength * key_player_boost(team_code)


def expected_goals(team_a: str, team_b: str) -> tuple[float, float]:
    """
    Returns (lambda_a, lambda_b) — expected goals for each team.

    Approach: relative strength ratio drives goal expectation so the
    stronger team scores more while total expected goals ≈ 2×BASE_GOAL_RATE.
    """
    s_a = _composite_strength(team_a)
    s_b = _composite_strength(team_b)

    # Elo win probability adjusts the ratio (pure Elo, for calibration)
    elo_a = TEAMS[team_a]["elo"]
    elo_b = TEAMS[team_b]["elo"]
    p_a = elo_win_probability(elo_a, elo_b)

    ratio = (s_a / s_b) ** 0.5 * (p_a / (1 - p_a + 1e-9)) ** 0.15
    lambda_a = BASE_GOAL_RATE * ratio / (1 + ratio) * 2
    lambda_b = BASE_GOAL_RATE / (1 + ratio) * 2

    # Attack / defense modifier
    atk_a = TEAMS[team_a]["attack"] / 7.0
    def_b = TEAMS[team_b]["defense"] / 7.0
    atk_b = TEAMS[team_b]["attack"] / 7.0
    def_a = TEAMS[team_a]["defense"] / 7.0

    lambda_a *= (atk_a / def_b) ** 0.3
    lambda_b *= (atk_b / def_a) ** 0.3

    return max(lambda_a, 0.1), max(lambda_b, 0.1)


def simulate_match(
    team_a: str,
    team_b: str,
    knockout: bool = False,
    rng: np.random.Generator | None = None,
) -> tuple[int, int, str | None]:
    """
    Simulate one match. Returns (goals_a, goals_b, penalty_winner).

    In knockout mode draws go to extra time then penalties.
    penalty_winner is the team code that won on penalties (or None).
    """
    if rng is None:
        rng = _RNG

    la, lb = expected_goals(team_a, team_b)
    goals_a = int(rng.poisson(la))
    goals_b = int(rng.poisson(lb))

    penalty_winner = None

    if knockout and goals_a == goals_b:
        # Extra time: each team has ~30% chance to score again
        et_a = int(rng.poisson(la * 0.30))
        et_b = int(rng.poisson(lb * 0.30))
        goals_a += et_a
        goals_b += et_b

        if goals_a == goals_b:
            # Penalties: stronger team (higher Elo) wins slightly more often
            p_a = elo_win_probability(TEAMS[team_a]["elo"], TEAMS[team_b]["elo"])
            penalty_winner = team_a if rng.random() < p_a else team_b

    return goals_a, goals_b, penalty_winner


def match_probabilities(team_a: str, team_b: str, n: int = 50_000) -> dict:
    """
    Monte-Carlo estimated probabilities for a single match (group stage).
    Returns dict with win_a, draw, win_b, expected_goals_a, expected_goals_b.
    """
    rng = np.random.default_rng(seed=42)
    la, lb = expected_goals(team_a, team_b)
    goals_a = rng.poisson(la, n)
    goals_b = rng.poisson(lb, n)

    win_a = float(np.mean(goals_a > goals_b))
    draw = float(np.mean(goals_a == goals_b))
    win_b = float(np.mean(goals_a < goals_b))

    return {
        "win_a": win_a,
        "draw": draw,
        "win_b": win_b,
        "xg_a": la,
        "xg_b": lb,
    }
