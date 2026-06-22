# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The game looked really clean with only a few components, a settings sidebar to toggle the diffuculty, the actual game, and the debugger box to help debug the game.

- List at least two concrete bugs you noticed at the start

  (for example: "the hints were backwards").

  The two concrete bugs I noticed at the start were that the hints were backwards, and changing the difficulty doesn't correcly alter the contraints.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| guess of 50 | "Go Lower!" hint becasue the target is 43| "Go Higher!"| None |
| guess of 32 | "Go Higher!" | "Go Lower!" | None |
| "Normal" mode to "Easy" mode| Range should be 1 to 20| Range shown is 1 to 100| None |
| "Normal" mode to "Easy" mode| Number of attemps goes up | Number of attempts goes down | None |
| clicked new game | All values refreshed and a new game starts | Wasn't allowed to give new guesses | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I only used Claude Clode to fix the glitches in the project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The AI gave the right suggestion when fixing the glitch of the hints being backwards. It recommended a fix of switching return strings "Go Lower" to "Go Higher" and vice versa. I verified the result by asking it to explain its logic behind the suggestion, and also ran the game again to officially test the fix. The bug was fixed and hints were being displayed appropriately.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI suggestions were never really incorrect or misleading, however, there were times were the AI would pick up certain bonus bugs not related to my prompt. For instance, it tried fixing the bug with the "New Game" button, when I was asking it to fix the bug concerning the difficulty ranges and attempts. To fix, I would be more specfic with my prompting so that the AI doesn't get distracted from the goal.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

After each proper fix in the code, I refreshed the app and tested out the functionality corresponding to the fix.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

Once I switched the return statements in the check_guess function, I refreshed the browser page, and entered two wrong guesses. After submitting each guess, it displayed a "📉 Go HIGHER!" when the number is smaller and a "📉 Go LOWER!" message for a bigger number. This showed that the code was fixed and the applied logic fits the game's intention.

- Did AI help you design or understand any tests? How?

I didn't really understand how I can create certain pytests for a bug which can be easily tested by running the app itself, for which AI helped me design the pytests. The main issue that I realized was that there was a clear gap with the tests imported from logic_utils.py, which only had placeholders. So, AI helped me understand that the code that needs to be tested should be pasted in the respective test functions, which will be imported test_game_logic.py to perform the tests.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

For streamlit reruns, I would say that every interaction and modification will cause the entire script to be rerun to keep the app updated.
For sessions states, I would highlight its similarity to a memory, which allows you store variables and data that needs to persist across the different tests and runs.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

A prompting strategy I realized would e really beneficial in any siutation was to always ask for its thought process before proceeding with the fix, it will be hard to trace back if we just blindly accept them. While prompting, it is also important that you are being specific with the bug to ensure the AI doesn't produce any unnecessary complications.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time, I would try to make better prompts and ask it to be more descriptive by adding comments to not lose track of all the changes occuring in the code.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

I realized AI can be a tool that can either enhace your understanding of certain problems, and help you learn new implementations of code, while also becoming a detrimental tool if not used as a learning tool. So, AI generated code is great if used correctly.
