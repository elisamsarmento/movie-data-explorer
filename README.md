# 🎬 Movie Data Explorer

An interactive movie data exploration tool that uses film APIs to generate visual analyses of movie ratings by genre or individual titles.

---

## 🚀 Features

### Genre Search
Search for movies by genre and generate visual insights, including:
- Rating distribution (histogram)
- Top 10 highest-rated movies in the genre

### Movie Search
Analyze a specific movie and compare its ratings across different sources:
- IMDb
- Rotten Tomatoes
- Metacritic

---

## 📊 Rating Visualizations

The project automatically generates charts saved in the `images/` folder:

- **rating_distribution.png**  
  Distribution of ratings for the selected genre.

- **genre_ranking.png**  
  Top 10 highest-rated movies within the genre.

- **movie_ratings.png**  
  Comparison of ratings from different sources for a specific movie.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data manipulation and analysis  
- **Matplotlib / Seaborn** – Data visualization  
- **Movie APIs**
  - OMDb API
  - TMDb API

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/movie-data-explorer.git
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Run the program:
```bash
python main.py
```
