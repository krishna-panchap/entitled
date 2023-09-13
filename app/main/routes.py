from flask import render_template, request, flash, session
from app.main import bp
import pandas as pd
from config import basedir
import os

SECRET_KEY = os.environ.get("SECRET_KEY")

@bp.route("/")
def root():
    return render_template("pass.html")


@bp.route("/index", methods=["POST", "GET"])
def index():
    usertable = pd.read_csv(basedir +  "/app/db/users.csv")
    if request.method == "POST":
        if request.form["submit"] == "namepass":
            username = request.form["username"]
            password = request.form["password"]
            if not username or not password:
                flash("Missing username or password", "inval")
                return render_template("pass.html")
            elif username not in usertable["name"].to_list():
                flash("wrong username", "inval")
                return render_template("pass.html")
            elif password != usertable.loc[usertable["name"] == username, "password"].iloc[0]:
                flash("wrong password", "inval")
                return render_template("pass.html")
            else:
                session["username"] = username
                session["password"] = password
                return render_template("inference.html")
    return render_template("pass.html")