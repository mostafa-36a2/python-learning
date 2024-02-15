# TODO:
# https://flask-login.readthedocs.io/en/latest/
# https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
# https://www.freecodecamp.org/news/build-secure-apis-with-flask-and-auth0/
# https://flask-httpauth.readthedocs.io/en/latest/
# https://www.django-rest-framework.org/
# https://graphene-python.org/
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    "user1": "pass1",
    "user2": "pass2",
}


@auth.verify_password
def verify_password(u, p):
    return users.get(u, None) == p


@app.route("/info", methods=["GET"])
@auth.login_required
def get_info():
    return jsonify(
        {
            "a": "b",
            "c": "d",
        }
    )


@app.route("/", methods=["GET"])
def index():
    return "Welcome to index\n"
