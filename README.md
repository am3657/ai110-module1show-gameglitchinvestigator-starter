# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
      The game's purpose was to showcase a traditional guessing game with limited attempts. However, there are certain bugs in the game which we need to investigate, hence the title Game Glitch Investigator.

- [ ] Detail which bugs you found.

1. The Go Higher and Lower Bug
   In a typical guessing game, when a person enters a larger number than the target, the game would give a hint that we need to go lower. However, this game is telling us to go higher. The same problem also exists if I give a lower number.

2. Difficulty bug
   When I was checking the differences between each difficulty, it was strange to see the easy mode allowing less attempts than the normal mode. Even the ranges didn't make sense because the range for normal was twice as long as the range for hard difficulty. Finally, the details for each difficulty mode does not mirror the ranges and number of attempts shown in the main page. For example, if the settings sidebar is showing that the easy mode uses a range from 1 to 20, the actual game allows you to guess from 1 to 100.

3. New game bug
   The new game button is broken because the game is not being refreshed completely. A new target is issued with attempts refreshed but it is not allowing me to attempt new numbers. It is persistently showing the message, "You won" despite hitting new game. A new game is not being created completely until the screen is refreshed.

- [ ] Explain what fixes you applied.

Fix #1:

The bug was in the check_guess function — when my guess was too high, the game told me to go higher, and when it was too low, it told me to go lower. That's completely backwards. The fix was simple: swap the hint messages so "Too High" points you down ("Go LOWER") and "Too Low" points you up ("Go HIGHER"). Once that was fixed, I also had to implement the function in logic_utils.py and update the tests to correctly unpack the tuple the function returns before the tests could actually run and pass.

Fix #2:

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

### Pytest to show that hints are now being displayed correclty.

platform win32 -- Python 3.13.7, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\akaas\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Codepath class\ai110-module1show-gameglitchinvestigator-starter
collected 3 items

tests/test_game_logic.py::test_winning_guess PASSED [ 33%]
tests/test_game_logic.py::test_guess_too_high PASSED [ 66%]
tests/test_game_logic.py::test_guess_too_low PASSED

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
