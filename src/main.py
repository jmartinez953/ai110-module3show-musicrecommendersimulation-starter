

from .recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Test the assignment's pop/happy profile.
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(
        f"\nUser profile: genre={user_prefs['genre']}, "
        f"mood={user_prefs['mood']}, energy={user_prefs['energy']:.2f}"
    )
    print("\nTop recommendations:\n")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} — Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
