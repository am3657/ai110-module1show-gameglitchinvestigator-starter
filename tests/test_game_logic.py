from logic_utils import check_guess, get_range_for_difficulty

def test_range_easy():
    # Easy difficulty should return a range of 1 to 20
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    # Normal difficulty should return a range of 1 to 100
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_range_hard():
    # Hard difficulty should return a range of 1 to 50
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_range_unknown():
    # An unrecognized difficulty should fall back to the default range of 1 to 100
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
