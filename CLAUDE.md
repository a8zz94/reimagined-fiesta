# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A FIFA World Cup 2026 prediction "super computer" built with Python + Streamlit. It simulates the full 48-team tournament 100,000 times using a Poisson goal-scoring model driven by composite team strength (Elo, form, squad quality, WC experience). The result is win/advancement probabilities for every team across every stage.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app (opens in browser at http://localhost:8501)
streamlit run app.py

# Run all tests
pytest

# Run a single test file
pytest tests/test_elo.py -v

# Run a single test
pytest tests/test_elo.py::test_expected_score_equal_teams -v
```

No build step required — pure Python.

## Architecture

```
app.py                    # Streamlit home page; hosts get_simulation_results() cache
pages/
  1_🏆_Overview.py        # Championship probability charts for all 48 teams
  2_📊_Groups.py          # Group standings and advancement probabilities
  3_⚔️_Simulator.py       # Head-to-head match predictor + live simulation
  4_👥_Teams.py           # Individual team deep-dive (squad, radar, round probs)
src/
  data/
    teams.py              # TEAMS dict — 48 teams with Elo, attack, defense, form, wc_experience
    players.py            # SQUADS dict — full player detail for top 12 teams; SQUAD_SUMMARY for rest
    fixtures.py           # group_fixtures(), all_group_fixtures(), THIRD_PLACE_SLOTS
  engine/
    elo.py                # Elo update formula, win_probability(), K-factors
    predictor.py          # expected_goals(), simulate_match(), match_probabilities()
    simulator.py          # run_simulation() — full Monte Carlo engine
```

### Data flow

1. `run_simulation(n=100_000)` in `simulator.py` drives everything — it calls `simulate_match()` for every fixture, builds group tables, selects the 32 advancing teams (top 2 per group + 8 best third-place), then runs knockout rounds recursively.
2. `simulate_match()` in `predictor.py` computes `expected_goals()` via a composite strength formula, samples from a Poisson distribution, and handles extra time + penalties for knockout ties.
3. `expected_goals()` blends Elo win probability, attack/defense ratings, form, squad quality, and WC experience into per-team lambda values for the Poisson sampler.
4. `get_simulation_results()` in `app.py` is a `@st.cache_data` wrapper — all four pages import and call it. Results are computed once and shared across the entire session.

### Composite strength formula (`predictor.py`)

```
strength = 0.40 × (elo/1800) + 0.25 × (form/10) + 0.20 × (squad_avg/80) + 0.15 × (wc_exp/10)
```
Then multiplied by `key_player_boost()` (±10% based on key-player average rating vs 85 baseline).

### Adding / updating team data

- Edit `src/data/teams.py` — each team is a dict entry in `TEAMS` with keys: `elo`, `attack`, `defense`, `form`, `wc_experience`, `group`, `confederation`, `fifa_ranking`, `flag`.
- Edit `src/data/players.py` — add full squad lists to `SQUADS` (for top teams) or summary entries in `SQUAD_SUMMARY`.
- Group assignments are in `TEAMS[code]["group"]` — change the `"group"` value to reassign a team.

### WC 2026 format

48 teams in 12 groups (A–L) of 4. Top 2 from each group + 8 best third-placed teams advance (32 total). Knockout: R32 → R16 → QF → SF → Final. Draws in knockout go to extra time then penalties.
