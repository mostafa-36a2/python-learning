# This file will have the function to create the app, which will initialize the database and register the blueprints.

import functools

from flask import Flask
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemt so we can use it later in our models


db = SQLAlchemy()


def create_app():
    import os

    dirname = os.path.dirname(__file__)
    # https://stackoverflow.com/questions/31002890/how-to-reference-a-html-template-from-a-different-directory-in-python-flask
    app = Flask("my_app", template_folder=os.path.join(dirname, "templates"))

    # https://flask.palletsprojects.com/en/3.0.x/config/
    app.config["SECRET_KEY"] = "MY_SECRET_KEY"
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
