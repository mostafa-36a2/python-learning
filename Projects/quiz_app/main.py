import flask

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/")
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    with open(
        "/home/mostafa/Documents/Python/Lessons/Projects/quiz_app/data.txt", "r"
    ) as file:
        txt = file.read()
        qa = eval(txt)

    response = jsonify(qa)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# main driver function
if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
