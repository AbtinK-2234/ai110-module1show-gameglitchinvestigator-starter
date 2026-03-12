import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug verification: difficulty ranges scale correctly ---

def test_hard_range_larger_than_normal():
    # Hard should have a larger range than Normal to be more difficult
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_easy_range_smallest():
    # Easy should have the smallest range
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high


# --- Bug verification: parse_guess rejects out-of-range values ---

def test_parse_guess_rejects_below_range():
    ok, value, err = parse_guess("-5", 1, 100)
    assert ok is False
    assert err == "Please guess between 1 and 100."

def test_parse_guess_rejects_above_range():
    ok, value, err = parse_guess("200", 1, 100)
    assert ok is False
    assert err == "Please guess between 1 and 100."

def test_parse_guess_accepts_valid_input():
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50


# --- Bug verification: update_score uses correct attempt number ---

def test_score_win_first_attempt():
    # Winning on attempt 1 should give 90 points (100 - 10*1), not 80
    score = update_score(0, "Win", 1)
    assert score == 90

def test_score_win_second_attempt():
    # Winning on attempt 2 should give 80 points (100 - 10*2)
    score = update_score(0, "Win", 2)
    assert score == 80


# --- Bug verification: Too High always penalizes ---

def test_score_too_high_even_attempt():
    # "Too High" on an even attempt should still penalize, not award points
    score = update_score(50, "Too High", 2)
    assert score == 45

def test_score_too_high_odd_attempt():
    # "Too High" on an odd attempt should also penalize
    score = update_score(50, "Too High", 3)
    assert score == 45

def test_score_too_low_penalizes():
    # "Too Low" should always penalize -5
    score = update_score(50, "Too Low", 1)
    assert score == 45
