import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read song dictionaries from a CSV file and convert numeric fields."""
    songs = []
    numeric_fields = (
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
    )

    with open(csv_path, newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["id"] = int(row["id"])
            for field in numeric_fields:
                row[field] = float(row[field])
            songs.append(row)

    return songs



def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a song's mood-and-energy score and explanatory reasons."""
    score = 0.0
    reasons = []

    preferred_mood = user_prefs["mood"].strip().lower()
    song_mood = song["mood"].strip().lower()
    target_energy = float(user_prefs["energy"])
    song_energy = float(song["energy"])

    if not (0.0 <= target_energy <= 1.0 and 0.0 <= song_energy <= 1.0):
        raise ValueError("User and song energy must be between 0 and 1.")

    if song_mood == preferred_mood:
        score += 60.0
        reasons.append(f"Mood match: {song_mood} (+60.00)")
    else:
        reasons.append(f"Mood mismatch: {song_mood} vs {preferred_mood} (+0.00)")

    energy_distance = abs(song_energy - target_energy)
    energy_points = 40.0 * (1.0 - energy_distance)
    score += energy_points
    reasons.append(
        f"Energy distance: {energy_distance:.2f} (+{energy_points:.2f})"
    )

    return score, reasons







def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top k with explanations."""
    if k <= 0:
        return []

    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda result: (-round(result[1], 10), int(result[0]["id"])))
    return scored_songs[:k]