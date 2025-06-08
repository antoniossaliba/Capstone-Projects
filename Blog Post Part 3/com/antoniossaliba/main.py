from flask import *
import datetime as dt
import sqlite3
from flask_login import *
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "TOPSECRETKEY"
login_manager = LoginManager()
login_manager.init_app(app)

TARGETTED_USER_ID = 0

db = sqlite3.connect("posts.db")
cursor = db.cursor()
all_ids = cursor.execute("SELECT * FROM id_table")
for id in all_ids:
    TARGETTED_USER_ID = id[0]
    break

class User(UserMixin):
    def __init__(self, id, email, password, name):
        self.id = id
        self.email = email
        self.password = password
        self.name = name

def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        g.user = current_user
        if g.user is None:
            return "<h1>Login/Register before!<h1/>"
        else:
            if g.user.id != 1:
                return "<h1>Unauthorized. You are not an admin."
            return function(*args, **kwargs)
    return decorated_function

@login_manager.user_loader
def load_user(user_id):
    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    all_users = cursor.execute("SELECT * FROM users")
    for user in all_users:
        if user[0] == int(user_id):
            return User(user[0], user[1], user[2], user[3])
    return None

@app.route('/')
def get_all_posts():
    if current_user.is_authenticated:
        db = sqlite3.connect("posts.db")
        cursor = db.cursor()
        blogs = cursor.execute("SELECT * FROM blogs")
        posts = []
        for blog in blogs:
            posts.append(blog)
            global TARGETTED_USER_ID
        return render_template("index.html", all_posts=posts, logged_in=current_user.is_authenticated, user_id=TARGETTED_USER_ID)
    return redirect("/menu")

@app.route('/post/<int:post_id>')
@login_required
def show_post(post_id):
    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    posts = cursor.execute("SELECT * FROM blogs WHERE id = ?", [post_id])
    requested_post = None
    for post in posts:
        requested_post = post
        break
    global TARGETTED_USER_ID
    return render_template("post.html", post=requested_post, logged_in=current_user.is_authenticated, user_id=TARGETTED_USER_ID)

@app.route("/new-post", methods=["GET", "POST"])
@login_required
@admin_only
def add_new_post():
    if request.method == "GET":
        return render_template("make-post.html", h1="New Post", logged_in=current_user.is_authenticated)
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
@login_required
@admin_only
def edit_post(id):
    if request.method == "GET":
        db = sqlite3.connect("posts.db")
        cursor = db.cursor()
        blogs = cursor.execute("SELECT * FROM blogs WHERE id = ?", [id])
        the_blog = None
        for blog in blogs:
            the_blog = blog
            break
        return render_template("make-post.html", id=id, blog=the_blog, h1="Edit Post", logged_in=current_user.is_authenticated)
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
@login_required
@admin_only
def delete_post(id):
    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM blogs WHERE id = ?", [id])
    db.commit()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    entered_email = request.form["email"]
    entered_password = request.form["password"]
    entered_name = request.form["name"]

    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    users = cursor.execute("SELECT * FROM users WHERE email = ?", [entered_email])
    counter = 0

    for user in users:
        counter += 1

    if counter != 0:
        flash("Email already exists.", "danger")
        return redirect("/login")
    else:
        flash("Registration successful.", "success")
        cursor.execute("INSERT INTO users (email, password, name) VALUES (?, ?, ?)",
                       [entered_email, generate_password_hash(entered_password), entered_name])
        db.commit()
        all_users = cursor.execute("SELECT * FROM users WHERE email = ?", [entered_email])
        user_id = 0
        for user in all_users:
            user_id = user[0]
            break
        global TARGETTED_USER_ID
        TARGETTED_USER_ID = user_id
        cursor.execute("UPDATE id_table SET id = ?", [TARGETTED_USER_ID])
        db.commit()
        login_user(load_user(user_id))
        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    entered_email = request.form["email"]
    entered_password = request.form["password"]

    db = sqlite3.connect("posts.db")
    cursor = db.cursor()
    all_users = cursor.execute("SELECT * FROM users WHERE email = ?", [entered_email])
    counter = 0
    u = None
    for user in all_users:
        counter += 1
        u = user
    if counter == 0:
        flash("Email does not exist register instead.", 'danger')
        return redirect("/register")
    else:
        if u[1] == entered_email and check_password_hash(u[2], entered_password):
            global TARGETTED_USER_ID
            TARGETTED_USER_ID = u[0]
            cursor.execute("UPDATE id_table SET id = ?", [TARGETTED_USER_ID])
            db.commit()
            login_user(load_user(u[0]))
            return redirect("/")

    flash("Email or password are wrong!", "danger")
    return redirect("/login")

@app.route("/about")
@login_required
def about():
    return render_template("about.html", logged_in=current_user.is_authenticated)

@app.route("/contact")
@login_required
def contact():
    return render_template("contact.html", logged_in=current_user.is_authenticated)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/menu")

@app.route("/menu")
def menu():
    if not current_user.is_authenticated:
        return render_template("menu.html")
    return "<h1>You are logged in.<h1/>"


if __name__ == "__main__":
    app.run(debug=True)
