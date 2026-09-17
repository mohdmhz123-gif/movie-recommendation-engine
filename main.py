from movies import movies


def recommend_movies(movies, genre, minimum_rating):
    recommendations = []

    for movie in movies:
        for movie_genre in movie["genre"]:
            if genre == movie_genre.lower() and movie["rating"] >= minimum_rating:
                recommendations.append(movie)
                break

    return recommendations


def get_available_genres(movies):
    genres = set()

    for movie in movies:
        for genre in movie["genre"]:
            genres.add(genre.lower())

    return genres


available_genres = get_available_genres(movies)


while True:
    genre = input("Enter your favourite genre: ").strip().lower()

    if genre not in available_genres:
        print("\nGenre not found.")
        print("Available genres:")
        
        for available_genre in sorted(available_genres):
            print(f"- {available_genre.title()}")

    else:
        break


while True:
    try:
        minimum_rating = float(input("Enter minimum rating (0-10): "))

        if minimum_rating < 0 or minimum_rating > 10:
            print("Please enter a rating between 0 and 10.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")


recommendations = recommend_movies(
    movies,
    genre,
    minimum_rating
)


recommendations = sorted(
    recommendations,
    key=lambda movie: movie["rating"],
    reverse=True
)


print("\nRecommended Movies:\n")


position = 1

for movie in recommendations:
    print(f"{position}. {movie['title']} — {movie['rating']} ⭐")
    position += 1


if not recommendations:
    print("No highly-rated movies found.")