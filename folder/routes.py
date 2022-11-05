from flask import Blueprint, jsonify, request

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

@point.route("/operation", methods=["POST"])
def operation():
    info = request.json
    keys = [i for i in info.keys()]
    data = {}
    for i in keys:
        data[i] = info.get(i)
    try:
        if "add" in data["operation_type"] :
            if data["x"] == None or data["x"] == 0 or data['y']==None or data["y"]==0:
                return jsonify({"detail": "checking out operations"})
            else:
                try:
                    result = float(data["x"]) + float(data["y"])
                    d= {
                        "operation_type" : "addition",
                        "result":result
                    }
                except :
                    return jsonify({"detail":"letters/operation n0t supported"}), 400

        elif "sub" in data["operation_type"] or "minus" in data["operation_type"]:
            if data["x"] == None or data["x"] == 0 or data['y']==None or data["y"]==0:
                return jsonify({"detail": "checking out operations"})
            else:
                try:
                    result = float(data["x"]) - float(data["y"])
                    d= {
                        "operation_type" : "subtraction",
                        "result":result
                    }
                except :
                    return jsonify({"detail":"letters/operation n0t supported"}), 400

        elif "mul" in data["operation_type"] :
            if data["x"] == None or data["x"] == 0 or data['y']==None or data["y"]==0:
                return jsonify({"detail": "checking out operations"})
            else:
                try:
                    result = float(data["x"]) * float(data["y"])
                    d= {
                        "operation_type" : "multiplication",
                        "result":result
                    }
                except :
                    return jsonify({"detail":"letters/operation n0t supported"}), 400
        d["slackUsername"] = "smalldev"
        return jsonify(d)
    except KeyError as e:
        return jsonify({"detail":f"{e} not provided"})