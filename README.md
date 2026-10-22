# 🎵 Music Recommender Simulation

## Project Summary

MoodFirst 1.0 is a CLI-first music recommendation simulation built with Python. It loads 18 fictional songs from a CSV file and ranks them using the listener's preferred mood and intensity.

An exact mood match earns 70 points, while energy similarity contributes up to 30 points. Each recommendation includes its score and an explanation. I evaluated four user profiles and temporarily removed mood scoring to explore how the rules affect results.


---



## How The System Works

Real-world recommendation systems predict what people might enjoy using user behavior and information about the content. Collaborative filtering learns from patterns across users, while content-based filtering compares content attributes with a user's preferences. My simulation will use content-based filtering, prioritizing mood and intensity.

### Dataset and User Profile

The expanded catalog contains 18 fictional songs with different genres, moods, and energy levels. Their numerical attributes are illustrative values rather than measurements of real recordings.

Each Song stores:
- Identification: id, title, and artist.
- Scoring features: mood and energy.
- Other available attributes: genre, tempo_bpm, valence, danceability, and acousticness.

The initial user preferences dictionary is:
- genre: lofi
- mood: chill
- energy: 0.35

These correspond to favorite_genre, favorite_mood, and target_energy in the starter UserProfile class. That class also stores likes_acoustic. Genre and acoustic preferences will not affect the initial score.

### Algorithm Recipe

1. Load the songs from data/songs.csv and convert numerical fields to numbers.
2. Validate that song and user energy values are between 0 and 1. Trim surrounding spaces and ignore capitalization when comparing mood labels.
3. Loop through every song and award 70 points for an exact mood match, or 0 points otherwise.
4. Calculate energy points using: 30 × (1 − |song energy − user target energy|). The vertical bars mean absolute value, so energy values equally far above and below the target receive equal points.
5. Add mood points and energy points for a total score between 0 and 100. Other attributes contribute no points.
6. Keep each song together with its score and an explanation of its mood match and energy distance.
7. Rank all songs by descending score, using scores rounded to ten decimal places for sorting comparisons only. Break comparison ties by ascending numeric song ID. Keep the original scores in the results and display them to two decimal places.
8. Return the top K songs, or all available songs if fewer than K exist. The initial setting is K = 5.

The scoring rule evaluates one song. The ranking rule compares all scored songs to choose the recommendations.

### Data Flow

User preferences + song catalog → Load and validate → Score every song → Rank songs → Return top K recommendations

### Expected Biases and Limitations

The weights deliberately favor exact mood matches: a matching mood always outranks a nonmatching mood, regardless of energy similarity. This could exclude suitable songs labeled relaxed or focused when the user requests chill. Exact matching treats mood labels as separate categories and does not understand related meanings.

The small, manually created catalog and subjective feature values limit variety and influence the results. Ignoring genre allows recommendations across musical styles, but may suggest styles the listener dislikes. The system will not learn from likes, skips, or changing preferences.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

========================== test session starts ==========================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\jmart\OneDrive\Documents\GitHub\ai110-module3show-musicrecommendersimulation-starter
plugins: anyio-4.14.2
collected 2 items

tests\test_recommender.py ..                                       [100%]

=========================== 2 passed in 0.15s =========================
---

## Sample Recommendation Output

Running `python -m src.main` evaluates four profiles using the final weights: 70 points for mood and up to 30 for energy similarity. This excerpt shows the High-Energy Pop results:

```text
=== High-Energy Pop ===
User profile: genre=pop, mood=happy, energy=0.90

Top recommendations:

1. Sunrise City — Score: 97.60
   Reasons: Mood match: happy (+70.00); Energy distance: 0.08 (+27.60)

2. Rooftop Lights — Score: 95.80
   Reasons: Mood match: happy (+70.00); Energy distance: 0.14 (+25.80)

3. Storm Runner — Score: 29.70
   Reasons: Mood mismatch: intense vs happy (+0.00); Energy distance: 0.01 (+29.70)

4. Victory Lap — Score: 29.40
   Reasons: Mood mismatch: confident vs happy (+0.00); Energy distance: 0.02 (+29.40)

5. Gym Hero — Score: 29.10
   Reasons: Mood mismatch: intense vs happy (+0.00); Energy distance: 0.03 (+29.10)
```

The two happy songs rank first because mood matches receive 70 points. Remaining songs rank by energy similarity. Genre is displayed but does not contribute points.

---

## Experiments You Tried

I ran `python -m src.main` against the 18-song catalog using three distinct profiles and one adversarial profile. Each run returned five recommendations with scores and explanations.

### High-Energy Pop

```text

=== High-Energy Pop ===
User profile: genre=pop, mood=happy, energy=0.90

Top recommendations:

1. Sunrise City — Score: 96.80
   Reasons: Mood match: happy (+60.00); Energy distance: 0.08 (+36.80)

2. Rooftop Lights — Score: 94.40
   Reasons: Mood match: happy (+60.00); Energy distance: 0.14 (+34.40)

3. Storm Runner — Score: 39.60
   Reasons: Mood mismatch: intense vs happy (+0.00); Energy distance: 0.01 (+39.60)

4. Victory Lap — Score: 39.20
   Reasons: Mood mismatch: confident vs happy (+0.00); Energy distance: 0.02 (+39.20)

5. Gym Hero — Score: 38.80
   Reasons: Mood mismatch: intense vs happy (+0.00); Energy distance: 0.03 (+38.80)



```

Happy songs ranked first. Rock and hip hop also appeared because genre does not contribute points.

### Chill Lofi

```text


=== Chill Lofi ===
User profile: genre=lofi, mood=chill, energy=0.35

Top recommendations:

1. Library Rain — Score: 100.00
   Reasons: Mood match: chill (+60.00); Energy distance: 0.00 (+40.00)

2. Midnight Coding — Score: 97.20
   Reasons: Mood match: chill (+60.00); Energy distance: 0.07 (+37.20)

3. Spacewalk Thoughts — Score: 97.20
   Reasons: Mood match: chill (+60.00); Energy distance: 0.07 (+37.20)

4. Coffee Shop Stories — Score: 39.20
   Reasons: Mood mismatch: relaxed vs chill (+0.00); Energy distance: 0.02 (+39.20)

5. Letters From Home — Score: 38.80
   Reasons: Mood mismatch: nostalgic vs chill (+0.00); Energy distance: 0.03 (+38.80)




```

Library Rain matched both mood and energy exactly. Midnight Coding and Spacewalk Thoughts tied, with ascending song ID deciding their order. The ambient song remained competitive because genre is not scored.

### Deep Intense Rock

```text

=== Deep Intense Rock ===
User profile: genre=rock, mood=intense, energy=0.95

Top recommendations:

1. Gym Hero — Score: 99.20
   Reasons: Mood match: intense (+60.00); Energy distance: 0.02 (+39.20)

2. Storm Runner — Score: 98.40
   Reasons: Mood match: intense (+60.00); Energy distance: 0.04 (+38.40)

3. Quiet Fury — Score: 39.60
   Reasons: Mood mismatch: angry vs intense (+0.00); Energy distance: 0.01 (+39.60)

4. Victory Lap — Score: 37.20
   Reasons: Mood mismatch: confident vs intense (+0.00); Energy distance: 0.07 (+37.20)

5. Paper Lantern Parade — Score: 36.80
   Reasons: Mood mismatch: celebratory vs intense (+0.00); Energy distance:0.08 (+36.80)




```


From my musical intuition, Gym Hero ranking first feels a bit off because this profile requests rock. However, I find the result acceptable when the system clearly displays its reasons: both songs match the intense mood, and Gym Hero's energy is closer to the target. The explanation makes the tradeoff understandable, even though it does not remove the mismatch with my genre preference. I will keep the current weights for now because mood and intensity remain my main priorities.


Gym Hero, a pop song, outranked Storm Runner, a rock song. Both matched the intense mood, but Gym Hero was closer to the target energy. This follows the recipe but may surprise a listener expecting rock recommendations.

### Adversarial Test: High-Energy Chill

```text

=== High-Energy Chill ===
User profile: genre=lofi, mood=chill, energy=1.00

Top recommendations:

1. Midnight Coding — Score: 76.80
   Reasons: Mood match: chill (+60.00); Energy distance: 0.58 (+16.80)

2. Library Rain — Score: 74.00
   Reasons: Mood match: chill (+60.00); Energy distance: 0.65 (+14.00)

3. Spacewalk Thoughts — Score: 71.20
   Reasons: Mood match: chill (+60.00); Energy distance: 0.72 (+11.20)

4. Quiet Fury — Score: 38.40
   Reasons: Mood mismatch: angry vs chill (+0.00); Energy distance: 0.04 (+38.40)

5. Gym Hero — Score: 37.20
   Reasons: Mood mismatch: intense vs chill (+0.00); Energy distance: 0.07 (+37.20)




```

This profile combined a chill mood with the maximum allowed energy of 1.00. All three chill songs outranked the more energetic alternatives, despite large energy differences. This is a limitation of the chosen weights rather than an implementation bug: a mood match always earns more total points than a mood mismatch.


### Feature Removal Experiment and Final Weights

I temporarily removed mood scoring while keeping the original energy calculation worth up to 40 points. Three of the four profiles changed their first-place recommendation:

| Profile | Original 60/40 winner | Energy-only winner |
| --- | --- | --- |
| High-Energy Pop | Sunrise City | Storm Runner |
| Chill Lofi | Library Rain | Library Rain |
| Deep Intense Rock | Gym Hero | Quiet Fury |
| High-Energy Chill | Midnight Coding | Quiet Fury |

Removing mood made recommendations closer in intensity but did not consistently improve their fit with my preferences. In particular, High-Energy Chill recommended angry and intense songs instead of chill songs.

After reviewing the results, I decided to give intensity less weight. My final rule awards 70 points for an exact mood match and up to 30 points for energy similarity:

Energy points = 30 × (1 − |song energy − target energy|)

I restored mood scoring and verified the new scores across all four profiles. The rankings stayed the same as the original 60/40 version because both weight combinations make mood matches outrank all mismatches. Within each group, energy distance still determines the order. The change expresses my priorities through the scores; it does not demonstrate improved ranking accuracy.

The earlier profile outputs in this section document the original 60/40 baseline.











### Evaluation Scope

These results verify the functional `recommend_songs` implementation used by the CLI. The separate `Recommender.recommend` class method remains a placeholder.
---

## Limitations and Risks

The catalog contains only 18 fictional songs with illustrative feature values. It cannot represent the full variety of music or listener preferences.

Exact mood matches always outrank mismatches. Related moods such as chill and relaxed receive no partial credit, and some mood-energy combinations are missing from the catalog.

Genre, lyrics, and other musical attributes do not affect scores. The system does not learn from feedback, so the same preferences return the same ranking and may limit discovery.

The CLI uses the implemented load_songs, score_song, and recommend_songs functions. The separate Recommender class methods remain starter placeholders.

---

## Reflection

I learned that recommendation systems turn preferences into rankings through specific rules and data. A result can follow those rules correctly and still feel surprising. For example, Gym Hero outranked a rock song for the Deep Intense Rock profile because genre was not scored and its energy was closer to the target. Seeing the explanation helped me understand the result.

Removing mood scoring showed me that matching intensity alone did not capture the vibe I wanted. I chose final weights of 70 points for mood and 30 for energy. This changed scores but not the original rankings. I also learned that exact mood labels and a small catalog can limit discovery and serve some preferences poorly. Explanations make these limitations visible, but do not eliminate them.

See the [Model Card](model_card.md) for the full evaluation, limitations, and ideas for improvement.



