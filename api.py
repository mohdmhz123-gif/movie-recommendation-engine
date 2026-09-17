import requests
from dotenv import load_dotenv
import os


def get_movies():
    load_dotenv()

    url = "https://api.themoviedb.org/3/movie/popular"
    genre_url = "https://api.themoviedb.org/3/genre/movie/list"

    token = os.getenv("TMDB_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    genre_response = requests.get(genre_url, headers=headers)
    genre_data = genre_response.json()

    genre_map = {}

    for genre in genre_data["genres"]:
        genre_map[genre["id"]] = genre["name"]

    movies = []

    for movie in data["results"]:
        genres = []

        for genre_id in movie["genre_ids"]:
            genres.append(genre_map[genre_id])

        formatted_movie = {
            "title": movie["title"],
            "rating": movie["vote_average"],
            "overview": movie["overview"],
            "release_date": movie["release_date"],
            "poster": "https://image.tmdb.org/t/p/w500" + movie["poster_path"],
            "genre": genres
        }

        movies.append(formatted_movie)

    return movies