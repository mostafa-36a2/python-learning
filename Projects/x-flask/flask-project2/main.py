from flask import Flask, Response, jsonify

my_app = Flask(__name__)


@my_app.route("/names")
def names():
    return {
        "client": [{"id": 1, "name": "Client"}],
        "peers": [
            {"id": 1, "name": "Peer1"},
            {"id": 2, "name": "Peer2"},
            {"id": 3, "name": "Peer3"},
            {"id": 4, "name": "Peer4"},
            {"id": 5, "name": "Peer5"},
            {"id": 6, "name": "Peer6"},
        ],
    }


@my_app.route("/status/<direction_type>/<id>")
def status(direction_type, id):

    if direction_type == "client":
        d = {
            "direction_type": direction_type,
            "id": id,
            "state": "connected",
            "msg": "2022-01-01",
        }
    elif direction_type == "peer":
        d = {
            "direction_type": direction_type,
            "id": id,
            "state": "diconnected" if int(id) % 2 == 0 else "connected",
            "msg": "2022-01-01",
        }
    else:
        d = {"msg": f"unknown direction_type : {direction_type}", "state": "unknown"}

    resp = jsonify(d)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


if __name__ == "__main__":
    my_app.run()
