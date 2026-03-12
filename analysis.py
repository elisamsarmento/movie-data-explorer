import matplotlib.pyplot as plt
import seaborn as sns
def plot_genre_charts(df, genre):
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="rating", bins=10, kde=True, color="skyblue")
    
    # rating distribution
    df["rating"].plot(kind="hist", bins=10, edgecolor='black')

    plt.title(f"TMDb Rating Distribution - {genre}")
    plt.xlabel("Rating")
    plt.ylabel("Number of Movies")
    plt.tight_layout()
    plt.savefig("images/rating_distribution.png")
    plt.show()

    # top 10 movies in this genre
    df_sorted = df.sort_values(by="rating", ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=df_sorted, 
        y="title", 
        x="rating", 
        hue="title", # Cores diferentes para cada barra
        palette="viridis",
        legend=False
    )

    plt.title(f"Top 10 Movies - {genre}")
    plt.xlabel("")
    ax.bar_label(ax.containers[0], padding=3)
    plt.tight_layout()
    plt.savefig("images/genre_ranking.png")
    plt.show()

def plot_movie_ratings(df, title):
    df_temp = df.copy()
    df_temp['score'] = df_temp['score'].apply(lambda x: x * 10 if x <= 10 else x)

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    ax = sns.barplot(
        data=df_temp, 
        x="source", 
        y="score", 
        hue="source", 
        palette="magma",
        legend=False
    )

    plt.title(f"Ratings Comparison - {title}", fontsize=16)
    plt.ylabel("Score (0-100)")
    plt.xlabel("")
    plt.xticks(rotation=30, ha='right')
    plt.ylim(0, 110)

    plt.tight_layout()
    plt.savefig("images/movie_ratings.png")
    plt.show()