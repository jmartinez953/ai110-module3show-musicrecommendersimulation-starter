# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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
3. Loop through every song and award 60 points for an exact mood match, or 0 points otherwise.
4. Calculate energy points using: 40 × (1 − |song energy − user target energy|). The vertical bars mean absolute value, so energy values equally far above and below the target receive equal points.
5. Add mood points and energy points for a total score between 0 and 100. Other attributes contribute no points.
6. Keep each song together with its score and an explanation of its mood match and energy distance.
7. Rank all songs by descending score. Treat mathematically equal scores as ties and break ties by ascending numeric song ID. Round scores only for display.
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

You can add more tests in `tests/test_recommender.py`.

---


## Sample Recommendation Output

Running `python -m src.main` with the pop/happy verification profile produces:

```text
Loaded songs: 18

User profile: genre=pop, mood=happy, energy=0.80

Top recommendations:

1. Sunrise City — Score: 99.20
   Reasons: Mood match: happy (+60.00); Energy distance: 0.02 (+39.20)

2. Rooftop Lights — Score: 98.40
   Reasons: Mood match: happy (+60.00); Energy distance: 0.04 (+38.40)

3. Night Drive Loop — Score: 38.00
   Reasons: Mood mismatch: moody vs happy (+0.00); Energy distance: 0.05 (+38.00)

4. Open Highway — Score: 37.20
   Reasons: Mood mismatch: hopeful vs happy (+0.00); Energy distance: 0.07 (+37.20)

5. Paper Lantern Parade — Score: 37.20
   Reasons: Mood mismatch: celebratory vs happy (+0.00); Energy distance: 0.07 (+37.20)
```

The two happy songs rank highest because mood matches receive 60 points. Other songs rank by energy similarity. Open Highway and Paper Lantern Parade tie, so their numeric song IDs determine their order. Genre is displayed but does not contribute points.

This verification profile differs from the original chill/0.35 profile described in the design plan.



---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



