from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    db = sqlite3.connect("todos.db")
    cursor = db.cursor()
    todos = cursor.execute("SELECT * FROM todo ORDER BY id ASC")
    list_of_todos = []
    list_of_ids = []
    for todo in todos:
        list_of_ids.append(todo[0])
        list_of_todos.append(todo[1])
    return render_template("index.html", ids=list_of_ids, todos=list_of_todos, len=len(list_of_ids))

@app.route("/delete/<int:id>")
def delete_to_do(id):
    db = sqlite3.connect("todos.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM todo WHERE id=?", [id])
    db.commit()
    return redirect("/")

@app.route("/add", methods=["GET", "POST"])
def add_to_do():
    if request.method == "GET":
        return render_template("add.html")
    db = sqlite3.connect("todos.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO todo (td) VALUES (?)", [request.form["to_do"]])
    db.commit()
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_to_do(id):
    if request.method == "GET":
        return render_template("update.html", id=id)
    db = sqlite3.connect("todos.db")
    cursor = db.cursor()
    cursor.execute("UPDATE todo SET td = ? WHERE id = ?", [request.form["new_to_do"], id])
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)