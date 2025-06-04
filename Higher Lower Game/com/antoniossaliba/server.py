from flask import Flask
import random as rnd

RANDOM_NUMBER   = rnd.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def home():
    return f'<h1>Guess a number between 0 and 9</h1>'

@app.route("/<int:number>")
def check_for_number(number):
    if number < RANDOM_NUMBER:
        return f'<h1 style="color: red">Too low, try again!</h1>'
    elif number > RANDOM_NUMBER:
        return f'<h1 style="color: purple">Too high, try again!</h1>'
    return f'<h1 style="color: green">You found me!</h1>'

if __name__ == "__main__":
    app.run(debug=True)

