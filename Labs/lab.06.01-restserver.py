# create a server and flask for an api

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello World"

#Getall
@app.route('/movies', methods=['GET'])
def getAll():
  return "get all"

#get by id
@app.route('/movies/<int:id>', methods=['GET'])
def getById(id):
  return "find by ID"

#create
@app.route('/movies', methods=['POST'])
def createMovie():
  #read in json from body
  jsonstr = request.json
  return f"create {jsonstr}"

#update
@app.route('/movies/<int:id>', methods=['PUT'])
def update(id):
  jsonstr = request.json
  return f"update {id} {jsonstr}"

#delete
@app.route('/movies/<int:id>', methods=['DELETE'])
def delete(id):
  return f"delete {id}"


if __name__ == "__main__":
  app.run(debug = True)