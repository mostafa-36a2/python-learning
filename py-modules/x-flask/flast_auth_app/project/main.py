from base import create_app, db
from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app = create_app()
    app.run()
