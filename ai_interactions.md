# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

### Guided AI Assistance Log

I used AI chat for explanations, code suggestions, and evaluation. I pasted the code changes myself and ran the commands step by step. This log documents guided assistance, not a claim that I completed the autonomous agent workflow stretch feature.

<!-- Describe the goal you asked the agent to accomplish -->

Create 8 more songs with the same attributes the other songs have.


I had the ai implement score song and focus on the mood match and energy points.


Make reccomend songs score evey song, sort the result and return top.

**Prompts used:**

<!-- Paste the key prompts you gave the agent -->

Generate 8 fictional songs to expand my music recommender dataset. Use the exact headers: id,title,artist,genre,mood,energy,tempo_bpm,valence,danceability,acousticness. Use unique IDs from 11 through 18. Include genres other than pop, lofi, rock, ambient, jazz, synthwave, and indie pop, and moods other than happy, chill, intense, relaxed, moody, and focused. Keep energy, valence, danceability, and acousticness between 0 and 1, and use plausible tempos in beats per minute. Return valid CSV with no commas inside field values.


Implement score_song(user_prefs, song). Award 60 points for an exact mood match, ignoring capitalization and surrounding spaces. Award 40 * (1 - abs(song_energy - user_energy)) energy points. Give genre zero points. Validate that energy values are between 0 and 1. Return a tuple containing the numeric total score and a list of readable reasons. Explain every line.





Implement recommend_songs(user_prefs, songs, k) using score_song to evaluate every song. Return tuples containing the song dictionary, numeric score, and readable explanation. Sort by descending score, breaking ties by ascending numeric song ID, and return the top k results. Explain every line and the difference between .sort() and sorted().


For my Deep Intense Rock profile (genre=rock, mood=intense, energy=0.95), why does Gym Hero rank first at 99.20 while Storm Runner ranks second at 98.40? Explain the contributions of mood, energy, and genre using my current scoring rule. Does this indicate a bug or a consequence of my chosen weights?


Temporarily modify score_song so mood contributes zero points for every song. Keep energy_points = 40 * (1 - abs(song_energy - target_energy)), energy validation, and ranking unchanged. Include a reason explaining that mood scoring is disabled. Verify the resulting score range and explain how to restore the original logic.


**What did the agent generate or change?**

<!-- List the files edited, code generated, or commands run -->

Generated an output with 8 new songs using new genres and moods while keeping the existing columns.


Temp modification of scoring function
    if song_mood == preferred_mood:
        score += 60.0
        reasons.append(f"Mood match: {song_mood} (+60.00)")
    else:
        reasons.append(f"Mood mismatch: {song_mood} vs {preferred_mood} (+0.00)")



**What did you verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
Deleted some songs and made it create two new ones.



---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->



**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
