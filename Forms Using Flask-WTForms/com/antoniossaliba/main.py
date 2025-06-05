from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm(request.form, meta={'csrf': False})
    if request.method == "GET":
        return render_template("login.html", form=form)
    if form.email.data == "antonios.saliba1@gmail.com" and form.password.data == "1234567":
        return render_template("success.html")
    return render_template("denied.html")

if __name__ == "__main__":
    app.run(debug=True)

