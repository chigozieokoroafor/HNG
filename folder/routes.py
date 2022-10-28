from flask import Blueprint, jsonify

point = Blueprint("point", __name__, url_prefix="/api")

@point.route("/home", methods=["GET"])
def home():
    data = { 
        "slackUsername": "smalldev", 
        "backend": True, 
        "age": 20, 
        "bio": "smalldev is a backend developer using the Flask framework for this current project, currently a student at Obafemi Awolowo University" 
        }
    return jsonify(data), 200

