import requests
import pandas as pd
from analysis import plot_genre_charts, plot_movie_ratings
API_KEY_OMD = "1da87ae7"
API_KEY_TMDB = "9dfff90a5114b7610730903fa4dadc76"

genres = {
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "horror": 27,
    "romance": 10749,
    "scifi": 878
}

def search_movies(genre):

    if genre not in genres:
        print("Genre not supported.")
        return

    genre_id = genres[genre]

    movies = []

    for page in range(1,6):  # pega até 100 filmes

        url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY_TMDB}&with_genres={genre_id}&page={page}"

        response = requests.get(url)
        data = response.json()

        for movie in data["results"]:

            rating = movie["vote_average"]

            if rating != 0:

                movies.append({
                    "title": movie["title"],
                    "rating": rating
                })

    df = pd.DataFrame(movies)

    if df.empty:
        print("No movies found.")
        return

    print("\n📊 Statistics\n")

    print("Movies analyzed:", len(df))
    print("Average rating:", round(df["rating"].mean(),2))

    best = df.loc[df["rating"].idxmax()]
    worst = df.loc[df["rating"].idxmin()]

    print("Best movie:", best["title"], "-", best["rating"])
    print("Worst movie:", worst["title"], "-", worst["rating"])

    plot_genre_charts(df, genre)


def search_title(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY_OMD}"
    response = requests.get(url)
    data = response.json()
    print(data)
    if data["Response"] == "False":
        print("Filme não encontrado!")
        return
    print("\n🎬 Informações do filme\n")

    print("Título:", data["Title"])
    print("Ano:", data["Year"])
    print("Gênero:", data["Genre"])
    print("Diretor:", data["Director"])
    print("Nota IMDb:", data["imdbRating"])

    ratings_data = data.get("Ratings", [])
    ratings = []

    for r in ratings_data:

        source = r["Source"]
        value = r["Value"]

        if "%" in value:
            score = float(value.replace("%", ""))

        elif "/" in value:
            score = float(value.split("/")[0])

        else:
            score = float(value)

        ratings.append({
            "source": source,
            "score": score
        })

    df = pd.DataFrame(ratings)

    print("\n📊 Ratings\n")
    print(df)
    plot_movie_ratings(df, title)
