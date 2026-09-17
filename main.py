from api import get_movies

movies = get_movies()


def recommend_movies(movies, genre, minimum_rating):
    recommendations = []

    for movie in movies:
        score = 0
        genre_match = False

        if movie["rating"] < minimum_rating:
            continue

        for movie_genre in movie["genre"]:
            if genre == movie_genre.lower():
                score += 5
                genre_match = True
                break

        if movie["rating"] >= 9:
            score += 3
        elif 8 <= movie["rating"] < 9:
            score += 2
        else:
            score += 1

        result = {
            "title": movie["title"],
            "score": score,
            "rating": movie["rating"]
        }

        if genre_match:
            recommendations.append(result)

    return sorted(
        recommendations,
        key=lambda movie: movie["score"],
        reverse=True
    )


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
        minimum_rating = float(
            input("Enter minimum rating (0-10): ")
        )

        if minimum_rating < 0 or minimum_rating > 10:
            print("Please enter a rating between 0 and 10.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")


while True:
    try:
        number_of_recommendations = int(
            input("How many recommendations do you want? ")
        )

        if number_of_recommendations < 1:
            print("Please enter a number greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a whole number.")


recommendations = recommend_movies(
    movies,
    genre,
    minimum_rating
)


if len(recommendations) < number_of_recommendations:
    print(
        f"\nOnly {len(recommendations)} matching movies were found."
    )


recommendations = recommendations[:number_of_recommendations]


print("\nRecommended Movies:\n")


position = 1

for movie in recommendations:
    print(
        f"{position}. {movie['title']} — "
        f"{movie['rating']} ⭐ — "
        f"Score: {movie['score']}"
    )
    position += 1


if not recommendations:
    print("No highly-rated movies found.")