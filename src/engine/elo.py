"""
Elo rating system for international football.

K-factors follow FIFA / eloratings.net conventions.
Goal-difference multiplier widens the Elo swing for convincing wins.
"""

import math

# K-factors by match importance
K_WORLD_CUP = 60
K_CONTINENTAL = 50
K_QUALIFIER = 40
K_FRIENDLY = 20


def expected_score(rating_a: float, rating_b: float) -> float:
    """Expected score for team A (probability of win + 0.5 × probability of draw)."""
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def goal_diff_multiplier(gd: int) -> float:
    """
    Multiplier based on absolute goal difference, per eloratings.net formula.
    GD 0–1 → 1.0, GD 2 → 1.5, GD 3 → 1.75, GD 4+ → 1.75 + (GD-3)/8
    """
    if gd <= 1:
        return 1.0
    if gd == 2:
        return 1.5
    if gd == 3:
        return 1.75
    return 1.75 + (gd - 3) / 8


def update_ratings(
    rating_a: float,
    rating_b: float,
    goals_a: int,
    goals_b: int,
    k: int = K_WORLD_CUP,
) -> tuple[float, float]:
    """
    Returns updated (rating_a, rating_b) after a match result.
    Actual score: 1 for win, 0.5 for draw, 0 for loss.
    """
    exp_a = expected_score(rating_a, rating_b)
    exp_b = 1 - exp_a

    if goals_a > goals_b:
        actual_a, actual_b = 1.0, 0.0
    elif goals_a < goals_b:
        actual_a, actual_b = 0.0, 1.0
    else:
        actual_a, actual_b = 0.5, 0.5

    gd = abs(goals_a - goals_b)
    gdm = goal_diff_multiplier(gd)

    new_a = rating_a + k * gdm * (actual_a - exp_a)
    new_b = rating_b + k * gdm * (actual_b - exp_b)
    return new_a, new_b


def win_probability(rating_a: float, rating_b: float) -> tuple[float, float, float]:
    """
    Returns (p_win_a, p_draw, p_win_b) for a neutral-venue match.

    Derived from Elo expected score using empirical draw correction:
    draw probability peaks around 25-30% for closely-matched teams.
    """
    diff = rating_a - rating_b
    # Base win probability (no draw split)
    p_win_a_raw = 1 / (1 + 10 ** (-diff / 400))

    # Draw probability is highest when teams are equal; decays with Elo gap
    draw_base = 0.27
    draw_decay = 0.001
    p_draw = draw_base * math.exp(-draw_decay * abs(diff))

    # Redistribute remaining probability to win/loss
    remaining = 1 - p_draw
    p_win_a = p_win_a_raw * remaining
    p_win_b = (1 - p_win_a_raw) * remaining

    return p_win_a, p_draw, p_win_b
