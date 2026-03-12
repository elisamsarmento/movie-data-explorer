from api import search_movies, search_title

print("🎬 Movie Data Explorer\n")

while True:

    option = input("Search by genre or movie? (genre/movie/quit): ").lower()

    if option in ["genre", "g"]:

        genre = input("Which genre do you want? ").lower()
        print(f"Searching movies in {genre}...")
        search_movies(genre)

    elif option in ["movie", "m"]:

        title = input("Which movie do you want to search? ").lower()
        print(f"Searching information about {title}...")
        search_title(title)

    elif option in ["quit", "exit", "q"]:

        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")