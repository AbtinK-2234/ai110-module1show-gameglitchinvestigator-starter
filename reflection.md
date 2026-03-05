# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

At first, the game looked fine when I ran it as I could input values into the guess bar as intended. However, I started to notice something was off when I exceed the range and guessed a number higher than the range and the game would suggest that I guess an even higher value. I even looked at the debug info section of the game to verify, and realized it was broken since the actual value was a much lower number than the guesses I had originally put while the game was still prompting me to guess a higher number. 

1. One concrete bug was that if I guessed a number higher than the target, it would suggest me to guess a number even higher. Or, when I guessed a number lower than the target it would sometimes suggest a lower guess. 
2. Another concrete bug would be that when I lost or won, and wanted to start a new game, it wouldn't work. Essentially, a new game session wouldn't start since it would be stuck at the current win/loss game. 
3. Another bug was that I could guess a number outside of the range, and then the game would suggest to go lower. For example, I guessed -5 when I should guess a number in the range (1, 100), but the game suggested me to go lower.  
4. Also, when we change the range of values to work with by selecting different modes of difficulty, the heading or prompt of the game doesn't change. It is always asking "Guess a number between 1 and 100" but with a different number of attempts. 
5. Also I believe the ordering of the difficulties is mixed, since an easy difficulty ranges from (1,20), while normal is (1,100) and hard is (1,50) in addition to the number of attempts where easy gives less attempts than the normal difficulty. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
