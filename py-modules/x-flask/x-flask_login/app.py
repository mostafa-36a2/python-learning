# https://flask-login.readthedocs.io/en/latest/
import flask_login
from flask import Flask, request
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)

login_manager = LoginManager()

# Unfortunately, login_manager need flask app to work in
app = Flask("test_loging_user")

SECRET_KEY = "e288d5e4d616084eb8262baab341b0b987a4ccd0971bfd9b9cbc5d4f3a253089"

app.config["SECRET_KEY"] = SECRET_KEY

login_manager.init_app(app)


class User(UserMixin):
    # Use id, or implement get_id
    user_id: str
    email: str
    password: str
    name: str

    def __init__(self, user_id, email, password, name):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.name = name

    def __repr__(self):
        return f"{self.user_id}, {self.email}, {self.password}, {self.name}"

    def get_id(self):
        return self.user_id


# My database
user1 = User(user_id=1, email="mostafa@email.com", password="12345678", name="Mostafa")
user2 = User(user_id=2, email="mostafa2@email.com", password="9876543", name="Mosta")
user3 = User(user_id=3, email="mostafa3@email.com", password="powerful", name="Mosty")
users = {
    "1": user1,
    "2": user2,
    "3": user3,
}


@login_manager.user_loader
def load_user(user_id):
    # app.logger.info("load user")
    user = users.get(user_id)
    print("-----------> load_user: ", user)
    return user


@login_manager.unauthorized_handler
def unauthorized():
    # https://stackoverflow.com/questions/13531149/check-for-a-cookie-with-python-flask
    items = request.cookies.items()
    return f"unauthorized, {set(items)}"


@app.route("/login")
def login():
    user_id = request.args.get("user_id")
    if users.get(user_id):
        res = login_user(users[user_id])
        return f"User Logged in: {res}\n"
    return "Bad credentials\n"


@app.route("/")
def index():
    print(flask_login.current_user)
    return "Hello World"


@app.route("/settings")
@login_required
def settings():
    return f"Settings accessed, I hope you are authorized, current_user={current_user.name}"


@app.route("/logout")
@login_required
def logout():
    print(f"bye bye {current_user.name}")
    logout_user()
    return "Logout, redirect"
