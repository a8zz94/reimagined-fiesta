import numpy as np

from src.engine.predictor import expected_goals, simulate_match, match_probabilities


def test_expected_goals_stronger_team_scores_more():
    la, lb = expected_goals("ARG", "IDN")
    assert la > lb, "Argentina should outscore Indonesia on average"


def test_expected_goals_are_positive():
    for pair in [("ARG", "FRA"), ("BRA", "ENG"), ("IDN", "NZL")]:
        la, lb = expected_goals(*pair)
        assert la > 0 and lb > 0


def test_simulate_match_returns_non_negative_goals():
    rng = np.random.default_rng(seed=0)
    for _ in range(50):
        ga, gb, pen = simulate_match("ARG", "FRA", knockout=False, rng=rng)
        assert ga >= 0 and gb >= 0


def test_simulate_knockout_no_draw():
    rng = np.random.default_rng(seed=0)
    for _ in range(200):
        ga, gb, pen = simulate_match("ARG", "FRA", knockout=True, rng=rng)
        # In knockout a draw must be resolved by penalty winner
        if ga == gb:
            assert pen in ("ARG", "FRA")
        else:
            assert pen is None


def test_match_probabilities_sum_to_one():
    mp = match_probabilities("ESP", "GER", n=10_000)
    total = mp["win_a"] + mp["draw"] + mp["win_b"]
    assert abs(total - 1.0) < 0.01


def test_stronger_team_higher_win_probability():
    mp = match_probabilities("ARG", "IDN", n=20_000)
    assert mp["win_a"] > mp["win_b"]
