def get_range_for_difficulty(difficulty: str):

    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    # FIXME: Logic breaks here — Hard range (1-50) is smaller than Normal (1-100), making Hard easier than Normal
    #FIX: Using Copilot Agent mode, I have updated the range for "Hard" difficulty to be 1-100, which is larger than the "Normal" range of 1-50, making "Hard" appropriately more difficult than "Normal".
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # FIXME: Logic breaks here — no range validation allowed out-of-range guesses (e.g. -5)
    #FIX: Using Copilot Agent mode, I have added range validation to the parse_guess function, so now it correctly rejects guesses that are outside the specified low and high range, ensuring that only valid guesses are accepted.
    if value < low or value > high:
        return False, None, f"Please guess between {low} and {high}."
    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        # FIXME: Logic breaks here — hint messages were reversed (Go HIGHER shown when too high, Go LOWER when too low)
        #FIX: Using Copilot Agent mode, I have swapped the hint messages for "Too High" and "Too Low", so now it correctly shows "Go LOWER" when the guess is too high and "Go HIGHER" when the guess is too low.
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go HIGHER!"
        return "Too Low", "📉 Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # FIXME: Logic breaks here — uses (attempt_number + 1) instead of attempt_number, penalizing an extra attempt
        #FIX: Using Copilot Agent mode, I have removed the "+ 1" from the points calculation for a win, so now it correctly calculates points based on the actual attempt number without penalizing an extra attempt.
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    # FIXME: Logic breaks here — "Too High" inconsistently awards +5 on even attempts instead of always penalizing
    #FIX: Using Copilot Agent mode, I have removed the conditional that awards points for "Too High" on even attempts, so now it always penalizes -5 points for "Too High", consistent with "Too Low".
    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
