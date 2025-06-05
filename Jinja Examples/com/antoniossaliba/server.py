from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/<name>")
def rendering_data(name):
    response1 = requests.get(url="https://api.agify.io", params={"name": name})
    response1.raise_for_status()
    the_age = response1.json()["age"]
    response2 = requests.get(url="https://api.genderize.io", params={"name": name})
    response2.raise_for_status()
    the_gender = response2.json()["gender"]
    return render_template("index.html", the_age=the_age, the_gender=the_gender, the_name=name.title())

@app.route("/blog")
def rendering_blog():
    response = requests.get(url="https://api.npoint.io/fd37d10f7f614061dc56")
    response.raise_for_status()
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)

