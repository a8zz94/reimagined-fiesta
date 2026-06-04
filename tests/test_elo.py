from src.engine.elo import expected_score, win_probability, update_ratings, goal_diff_multiplier


def test_expected_score_equal_teams():
    assert expected_score(1800, 1800) == 0.5


def test_expected_score_stronger_team():
    assert expected_score(1900, 1800) > 0.5


def test_win_probability_sums_to_one():
    pa, pd, pb = win_probability(1900, 1800)
    assert abs(pa + pd + pb - 1.0) < 1e-9


def test_win_probability_symmetry():
    pa, pd, pb = win_probability(2000, 1800)
    pa2, pd2, pb2 = win_probability(1800, 2000)
    assert abs(pa - pb2) < 1e-9
    assert abs(pd - pd2) < 1e-9


def test_update_ratings_win_increases_winner():
    new_a, new_b = update_ratings(1800, 1800, 2, 0)
    assert new_a > 1800
    assert new_b < 1800


def test_update_ratings_draw_equal_teams():
    new_a, new_b = update_ratings(1800, 1800, 1, 1)
    assert abs(new_a - 1800) < 1e-6
    assert abs(new_b - 1800) < 1e-6


def test_goal_diff_multiplier():
    assert goal_diff_multiplier(0) == 1.0
    assert goal_diff_multiplier(1) == 1.0
    assert goal_diff_multiplier(2) == 1.5
    assert goal_diff_multiplier(3) == 1.75
    assert goal_diff_multiplier(4) > 1.75
