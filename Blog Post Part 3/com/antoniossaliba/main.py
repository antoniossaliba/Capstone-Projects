from flask import *
import datetime as dt
import sqlite3

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    blogs = cursor.execute("SELECT * FROM blogs")
    posts = []
    for blog in blogs:
        posts.append(blog)
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    posts = cursor.execute("SELECT * FROM blogs WHERE id = ?", [post_id])
    requested_post = None
    for post in posts:
        requested_post = post
        break
    return render_template("post.html", post=requested_post)

@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    if request.method == "GET":
        return render_template("make-post.html", h1="New Post")
    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    today = str(dt.datetime.today()).split(" ")[0].split("-")
    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    cursor.execute("INSERT INTO blogs (title, subtitle, date, body, author, img_url) VALUES (?, ?, ?, ?, ?, ?)",
                   [request.form["title"], request.form["subtitle"], f"{months[today[1]]} {today[2]}, {today[0]}", request.form["body"],
    request.form["author"], request.form["backgroundImage"]])
    db.commit()
    return redirect("/")

@app.route("/edit-post/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    if request.method == "GET":
        db = sqlite3.connect("posts.db")
        cursor = db.cursor()
        blogs = cursor.execute("SELECT * FROM blogs WHERE id = ?", [id])
        the_blog = None
        for blog in blogs:
            the_blog = blog
            break
        return render_template("make-post.html", id=id, blog=the_blog, h1="Edit Post")
    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    today = str(dt.datetime.today()).split(" ")[0].split("-")
    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    cursor.execute("UPDATE blogs SET title = ?, subtitle = ?, date = ?, body = ?, author = ?, img_url = ? WHERE id = ?",
                   [request.form["title"], request.form["subtitle"], f"{months[today[1]]} {today[2]}, {today[0]}",
                    request.form["body"],
                    request.form["author"], request.form["backgroundImage"], id])
    db.commit()
    return redirect(f"/post/{id}")

@app.route("/delete/<int:id>", methods=["GET"])
def delete_post(id):
    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM blogs WHERE id = ?", [id])
    db.commit()
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
