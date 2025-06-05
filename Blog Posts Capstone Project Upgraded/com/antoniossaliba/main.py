from flask import *
import requests
from smtplib import *
import os

app = Flask(__name__)

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

@app.route("/")
def home():
    response = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7")
    response.raise_for_status()
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject: New Message\n\nName: {request.form['name']}\nEmail: {request.form['email']}\n"
                                f"Phone: {request.form['phone-number']}\nMessage: {request.form['message']}")
    return render_template("contact.html", the_title="Message sent successfully!")

@app.route("/post/<int:post_id>")
def post(post_id):
    response = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7")
    response.raise_for_status()
    the_required_post = response.json()[post_id - 1]
    return render_template("post.html", post=the_required_post)

if __name__ == "__main__":
    app.run(debug=True)

