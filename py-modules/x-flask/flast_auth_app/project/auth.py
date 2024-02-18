from base import db
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user

# from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint("auth", __name__)

users = {
    "mostafa@email.com": "mypassword",
    "mostafa1@email.com": "mypasswor1",
    "mostafa2@email.com": "mypassword2",
    "mostafa3@email.com": "mypassword3",
}


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    # login code goes here
    email = request.form.get("email")
    password_provided = request.form.get("password")
    remember = True if request.form.get("remember") else False

    password = users.get(email)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not password or not password == password_provided:
        flash("Please check your login details and try again.")
        return redirect(
            url_for("auth.login")
        )  # if the user doesn't exist or password is wrong, reload the page

    login_user(user, remember=remember)
    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for("main.profile"))


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    # code to validate and add user to database goes here
    return redirect(url_for("auth.login"))


@auth.route("/logout")
def logout():
    return "Logout"
