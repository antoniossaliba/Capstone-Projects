from flask import *
import sqlite3
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")
API_READ_ACCESS_TOKEN = os.environ.get("API_READ_ACCESS_TOKEN")

@app.route("/")
def home():
    db = sqlite3.connect("my_movies.db")
    cursor = db.cursor()
    movies = cursor.execute("SELECT * FROM movies ORDER BY rating DESC")
    return render_template("index.html", movies=movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    the_movie_title = request.form["title"]
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_READ_ACCESS_TOKEN}"
    }
    response = requests.get(url="https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1",
                            headers=headers,
                            params={"query": the_movie_title})
    response.raise_for_status()
    return render_template("select.html", movies=response.json()["results"])

@app.route("/details/<int:id>")
def get_details(id):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_READ_ACCESS_TOKEN}"
    }
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{id}",
                            headers=headers)
    response.raise_for_status()
    the_title = response.json()["original_title"]
    the_year = response.json()["release_date"]
    the_description = response.json()["overview"]
    the_image_url = f"https://image.tmdb.org/t/p/original{response.json()['poster_path']}"
    db = sqlite3.connect("my_movies.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO movies (title, year, description, img_url) VALUES (?, ?, ?, ?)", [the_title,
                                                                                                  the_year,
                                                                                                  the_description,
                                                                                                  the_image_url])
    db.commit()
    movies = cursor.execute("SELECT id FROM movies WHERE title = ?", [the_title])
    user_id = 0
    for movie in movies:
        user_id = movie[0]
        break
    return render_template("edit.html", user_id=user_id)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "GET":
        return render_template("edit.html", user_id=id)
    db = sqlite3.connect("my_movies.db")
    cursor = db.cursor()
    cursor.execute("UPDATE movies SET rating = ?, revview = ? WHERE id = ?", [request.form["rating"],
                                                                              request.form["review"], id])
    db.commit()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    db = sqlite3.connect("my_movies.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM movies WHERE id=?", [id])
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

