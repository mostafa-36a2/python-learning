# https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
from flask import Flask, redirect, request, session, url_for

app = Flask(__name__)

SECRET_KEY = "e288d5e4d616084eb8262baab341b0b987a4ccd0971bfd9b9cbc5d4f3a253089"
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def index():
    if "username" in session:
        app.logger.info(f'User logged in as {session["username"]}')
        print(session)
        session["counter"] += 1
        return f'Logged in as {session["username"]}, counter : {session["counter"]}'
    return "You are not logged in"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["counter"] = 0
        return redirect(url_for("index"))
    return """
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    """


@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop("username", None)
    session.pop("counter", None)
    return redirect(url_for("index"))
