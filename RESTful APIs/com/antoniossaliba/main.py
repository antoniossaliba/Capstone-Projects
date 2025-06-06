from flask import *
import sqlite3
import random as rnd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def get_random_cafe():
    db = sqlite3.connect("cafes.db")
    cursor = db.cursor()
    total_number_of_cafes_inside_the_database = cursor.execute("SELECT COUNT(*) FROM cafe").fetchone()
    total = total_number_of_cafes_inside_the_database[0]
    if total < 1:
        return {"error": {"Not found": "Error occured! No results found!"}}
    random_counter = rnd.randint(1, total)
    start_counter = 1
    required_entry = None
    for cafe in cursor.execute("SELECT * FROM cafe"):
        if start_counter == random_counter:
            required_entry = cafe
            break
        start_counter += 1
    returned_json = {}
    attribute_list = ["id", "name", "map_url", "img_url", "location", "seats", "has_toilet", "has_wifi",
                      "has_sockets", "can_take_calls", "coffee_price"]
    idx = 0
    for entry in required_entry:
        returned_json[attribute_list[idx]] = entry
        idx += 1
    return {"cafe": returned_json}

@app.route("/all", methods=["GET"])
def get_all_cafes():
    db = sqlite3.connect("cafes.db")
    cursor = db.cursor()
    cafes = cursor.execute("SELECT * FROM cafe")
    all_cafes = []
    counter = 1
    for cafe in cafes:
        returned_json = {}
        returned_json["id"]             = cafe[0]
        returned_json["name"]           = cafe[1]
        returned_json["map_url"]        = cafe[2]
        returned_json["img_url"]        = cafe[3]
        returned_json["location"]       = cafe[4]
        returned_json["seats"]          = cafe[5]
        returned_json["has_toilet"]     = cafe[6]
        returned_json["has_wifi"]       = cafe[7]
        returned_json["has_sockets"]    = cafe[8]
        returned_json["can_take_calls"] = cafe[9]
        returned_json["coffee_price"]   = cafe[10]
        all_cafes.append({f"cafe {counter}": returned_json})
        counter += 1
    return all_cafes

@app.route("/search", methods=["GET"])
def get_by_search():
    db = sqlite3.connect("cafes.db")
    cursor = db.cursor()
    cafes = cursor.execute("SELECT * FROM cafe WHERE location = ?", [request.args.get("loc")])
    counter = 1
    json = {}
    for cafe in cafes:
        returned_json = {}
        returned_json["id"]             = cafe[0]
        returned_json["name"]           = cafe[1]
        returned_json["map_url"]        = cafe[2]
        returned_json["img_url"]        = cafe[3]
        returned_json["location"]       = cafe[4]
        returned_json["seats"]          = cafe[5]
        returned_json["has_toilet"]     = cafe[6]
        returned_json["has_wifi"]       = cafe[7]
        returned_json["has_sockets"]    = cafe[8]
        returned_json["can_take_calls"] = cafe[9]
        returned_json["coffee_price"]   = cafe[10]
        json[f"cafe {counter}"]         = returned_json
        counter += 1
    if json == {}:
        return {"error": {"Not found": "Error occured! No results found!"}}
    return json

@app.route("/add", methods=["POST"])
def add_cafe():
    db = sqlite3.connect("cafes.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO cafe (name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets,"
                   "can_take_calls, coffee_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [request.form["name"],
                                                                                           request.form["map_url"],
                                                                                           request.form["img_url"],
                                                                                           request.form["location"],
                                                                                           request.form["seats"],
                                                                                           request.form["has_toilet"],
                                                                                           request.form["has_wifi"],
                                                                                           request.form["has_sockets"],
                                                                                           request.form["can_take_calls"],
                                                                                           request.form["coffee_price"]])
    db.commit()
    return {"response": {"success": "Successfully added the new cafe."}}

@app.route("/update-price/<id>", methods=["PATCH"])
def update_price(id):
    db = sqlite3.connect("cafes.db")
    cursor = db.cursor()
    cafes = cursor.execute("SELECT * FROM cafe WHERE id = ?", [id])
    counter = 0
    for cafe in cafes:
        counter += 1
    if counter == 0:
        return {"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}}
    cursor.execute("UPDATE cafe SET coffee_price = ? WHERE id = ?", [request.args.get("coffee_price"), id])
    db.commit()
    return {"success": "Successfully updated the price."}

@app.route("/report-closed/<id>", methods=["DELETE"])
def delete_cafe(id):
    db = sqlite3.connect("cafes.db")
    cursor = db.cursor()
    cafes = cursor.execute("SELECT * FROM cafe WHERE id = ?", [id])
    counter = 0
    for cafe in cafes:
        counter += 1
    if counter == 0:
        return {"error": {"Not Found": "Sorry a cafe with that id was not found in the database."}}
    if request.args.get("api-key") != "TopSecretAPIKey":
        return {"error": "Sorry, that's not allowed. Make sure you have the correct api_key."}
    cursor.execute("DELETE FROM cafe WHERE id = ?", [id])
    db.commit()
    return {"success": "Successfully removed the closed cafe!"}

if __name__ == '__main__':
    app.run(debug=True)

