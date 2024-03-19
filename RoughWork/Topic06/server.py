from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello Kevin"

@app.route("/inquiry")
def inquiry():
  name = request.args["name"]
  return request.args

@app.route("/inbody", methods=["POST"])
def inbody():
  name = request.json["name"]
  age = request.json["age"]
  return f"you are {name} and you are {age} years old"

@app.route("/user")
def getuser():
  user= {
    'name': "andrew",
    'age' : 21
  }
  return jsonify(user)

if __name__ == "__main__":
  app.run(debug = True)