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

Fix #1: Backward hints

The bug was in the check_guess function — when my guess was too high, the game told me to go higher, and when it was too low, it told me to go lower. That's completely backwards. The fix was simple: swap the hint messages so "Too High" points you down ("Go LOWER") and "Too Low" points you up ("Go HIGHER"). Once that was fixed, I also had to implement the function in logic_utils.py and update the tests to correctly unpack the tuple the function returns before the tests could actually run and pass.

Fix #2: Displaying the wrong ranges for all the difficulty modes and number of attempts

The attempts counter was initialized to 1 instead of 0, making the display always show one fewer attempt than allowed. The in-game range prompt was also hardcoded to "1 and 100" regardless of difficulty, so I updated it to use the actual low and high variables. I also started moving the game logic into logic_utils.py and wrote pytest tests to verify each difficulty returns the correct number range.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Pick any difficulty mode you like from the settings sidebar
2. Guess a number from the given range in which the secret is present
3. Enter your guess and hit submit guess.
4. Repeat step 3 until you either find the secret or you have exhasuted your allowed attempts
5. Once the game is over, hit new game, and start over.

**Screenshot** _(optional)_: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

### Pytest to show that hints are now being displayed correclty.

> > python -m pytest tests/test_game_logic.py -v
> > ================================================ test session starts =================================================
> > platform win32 -- Python 3.13.7, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\akaas\AppData\Local\Programs\Python\Python313\python.exe
> > cachedir: .pytest_cache
> > rootdir: C:\Codepath class\ai110-module1show-gameglitchinvestigator-starter
> > collected 7 items

tests/test_game_logic.py::test_range_easy PASSED [ 14%]
tests/test_game_logic.py::test_range_normal PASSED [ 28%]
tests/test_game_logic.py::test_range_hard PASSED [ 42%]
tests/test_game_logic.py::test_range_unknown PASSED [ 57%]
tests/test_game_logic.py::test_winning_guess PASSED [ 71%]
tests/test_game_logic.py::test_guess_too_high PASSED [ 85%]
tests/test_game_logic.py::test_guess_too_low PASSED [100%]

================================================= 7 passed in 0.04s ==================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
      Some enhanced UI changes I would make here is that I would add more features concerning each diffuculty, and eventually make the UI itself more engaging for the user. Aside from the UI changes, I would ensure all the bugs are fixed in the app, making it a flawless game.
