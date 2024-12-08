from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = {}

with open("database.json", 'r') as f:
    data = json.load(f)


@app.route('/getStudent/<username>')
def getStudent(username):
    try:
        return jsonify({
        "message": "Student found!",
        "name": username,
        "age": data[username]["age"],
        "class": data[username]["class"],
        "status": 200
    }), 200
    except:
        return jsonify({
            "message": "Student not found!",
            "status": 201
        }), 201

    


@app.route('/addStudent')
def addStudent():
    username = request.args.get("username")
    cls = request.args.get("class")
    age = request.args.get("age")

    if not username or not cls or not age:
        return jsonify({
            "message": "All details not given!",
            "status": 201
        }), 201
    
    obj = {
        "username": username,
        "class": cls,
        "age": age,
    }

    data[username] = obj

    with open("database.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    
    return jsonify({
        "message": "Student Added Successfully!",
        "status": 200
    }), 200


if __name__ == '__main__':
    app.run(debug=True)