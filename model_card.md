# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**MoodFirst 1.0**

A music recommender that prioritizes mood, then matches the listener's preferred intensity.

---

## 2. Intended Use

MoodFirst suggests songs based on a listener's chosen mood and preferred intensity. It ranks songs from a small fictional catalog and explains each recommendation.


It is not designed to predict everyone's musical taste or power a real streaming service. It does not listen to audio, learn from user behavior, or determine a person's emotional state.

---

## 3. How the Model Works

MoodFirst compares each song with the listener's requested mood and energy. An exact mood match earns 70 points. Capitalization and surrounding spaces do not affect the match.

Energy similarity contributes up to 30 points. Songs closer to the listener's preferred intensity earn more points. Equal differences above and below the target earn equal points.

The system adds these points and ranks songs from highest to lowest score. It compares scores to ten decimal places when sorting and breaks ties using the lower song ID. It returns the requested number of songs with explanations.

Genre and other song attributes do not contribute points. The system uses fixed rules rather than a trained machine-learning model.

---

## 4. Data


The catalog contains 18 fictional songs stored in data/songs.csv. I expanded the original 10-song dataset by adding eight AI-generated songs.

Each song includes an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. Only mood and energy affect recommendation scores.

The catalog includes styles such as pop, lofi, rock, jazz, folk, metal, and salsa. Mood labels include happy, chill, intense, nostalgic, and hopeful.

The feature values are illustrative rather than measurements of real recordings. The small catalog cannot represent the full variety of music or listener preferences. Some moods have only one song, and combinations such as high-energy chill are missing.



---

## 5. Strengths


MoodFirst works well when the catalog contains songs that match both the requested mood and intensity. For example, Library Rain scored 100 for the Chill Lofi profile because both features matched exactly.

The explanations show how mood and energy contribute to each score. This makes surprising results easier to understand.

Different profiles produced different first-place recommendations in our tests. The system also handles capitalization and surrounding spaces consistently when comparing mood labels.



---

## 6. Limitations and Bias

My recommender strongly favors exact mood matches because mood contributes 70 points while energy contributes at most 30. In the High-Energy Chill experiment, low-energy chill songs outranked much more energetic songs with different mood labels, even though the user requested maximum intensity. Related labels such as relaxed and chill receive no partial credit, which can exclude songs a listener might enjoy. Repeated requests with the same profile return the same ranking, potentially limiting discovery beyond the preferred mood. This design may underserve listeners whose desired mood and intensity combination is not represented in the small catalog.

---

## 7. Evaluation

I tested four profiles against the 18-song catalog: High-Energy Pop (happy, energy 0.90), Chill Lofi (chill, energy 0.35), Deep Intense Rock (intense, energy 0.95), and High-Energy Chill (chill, energy 1.00). I checked each profile's top five songs, scores, and explanations. The comparisons below describe my final scoring rule: 70 points for a mood match and up to 30 points for energy similarity. Genre preferences are stored but do not affect scores.

### Comparisons Between Profiles

- **High-Energy Pop vs. Chill Lofi:** The pop profile ranked Sunrise City first, while Chill Lofi ranked Library Rain first. Their different mood and intensity preferences produced completely different top-five lists, which makes sense for upbeat versus gentle listening.

- **High-Energy Pop vs. Deep Intense Rock:** The happy profile placed Sunrise City and Rooftop Lights first, while the intense profile placed Gym Hero and Storm Runner first. Gym Hero also appeared fifth for High-Energy Pop because its energy was close to the target, even though its mood did not match. With only two happy songs in the catalog, the remaining places were filled using energy similarity.

- **High-Energy Pop vs. High-Energy Chill:** Although both requested high intensity, their first choices differed sharply. Happy songs led the pop profile, while low-energy chill songs led High-Energy Chill. This shows that matching mood matters more than matching intensity.

- **Chill Lofi vs. Deep Intense Rock:** Chill Lofi favored gentle songs such as Library Rain and Midnight Coding, while Deep Intense Rock favored Gym Hero and Storm Runner. Both mood and energy changed between these profiles, and their top-five lists had no songs in common. This fits their contrasting listening preferences.

- **Chill Lofi vs. High-Energy Chill:** Both profiles requested chill music, so the same three chill songs occupied the first three places. Raising the target energy from 0.35 to 1.00 moved Midnight Coding above Library Rain because it is more energetic. The remaining places changed from Coffee Shop Stories and Letters From Home to Quiet Fury and Gym Hero because those songs are closer to the higher energy target.

- **Deep Intense Rock vs. High-Energy Chill:** Their energy targets were close, but their requested moods differed. Gym Hero led the intense profile, while Midnight Coding led the chill profile. Quiet Fury appeared in both lists because of its high energy, but it could not outrank songs matching the requested mood.

### Surprises and Experiment

Gym Hero ranking above Storm Runner for Deep Intense Rock felt slightly off because Gym Hero is a pop song. However, its explanation made the result understandable: both songs matched the intense mood, and Gym Hero was closer to the requested energy. I accepted this tradeoff because mood and intensity are my main priorities.

I temporarily removed mood points while keeping energy worth up to 40 points. The winner changed for three of the four profiles: Storm Runner won High-Energy Pop, and Quiet Fury won both Deep Intense Rock and High-Energy Chill. Library Rain remained first for Chill Lofi. The experiment matched intensity more closely but lost the requested feeling in important cases.

After reviewing those results, I restored mood scoring and changed the weights from 60/40 to 70/30 to express my stronger preference for mood. Scores changed, but rankings stayed the same as the original version because both versions always place mood matches above mismatches. This was a preference decision, not evidence of improved accuracy.

These checks evaluated the functional recommend_songs implementation used by the CLI. They confirmed expected behavior for the tested profiles, but they do not establish accuracy for all listeners or real music.

---

## 8. Future Work

- Give partial mood credit to related labels, such as chill and relaxed, instead of requiring an exact match.
- Expand the catalog with more songs and mood-energy combinations, especially high-energy chill songs.
- Let listeners adjust the importance of mood, energy, and genre so recommendations better reflect their own priorities.
---

## 9. Personal Reflection

I learned that a recommender can follow its rules correctly and still produce a surprising suggestion. Gym Hero winning for the rock profile felt slightly off, but the explanation helped me understand and accept the result.

Removing mood scoring showed me how much the requested feeling matters to my preferences. I changed the weights to 70 points for mood and 30 for energy. This changed the scores but not the original rankings, which taught me that changing weights does not always change recommendations.

This project helped me see how recommendation rules and limited data shape what users discover. Clear explanations make those choices easier to understand, but they do not remove the system's limitations.