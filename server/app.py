"""
app.py - Flask-RESTful server that exposes toolbox.py as an API.

Each "Resource" is a class. Its methods (get, post, put, delete) are the
HTTP methods it responds to. api.add_resource() ties a class to a URL.

Endpoints
---------
POST   /api/analyze            {"text": "hello world"}
GET    /api/convert?value=100&unit=C
GET    /api/dice?sides=6&count=2
GET    /api/todos
POST   /api/todos              {"title": "Have fun at the workshop :D"}
PUT    /api/todos/<id>         (marks the item done)
DELETE /api/todos/<id>
"""
import requests

from src import toolbox

from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource

app = Flask(__name__)
CORS(app)
api = Api(app)

todos = toolbox.TodoList()

# Resources


class Cats(Resource):
    def get(self):
        res = requests.get("https://catfact.ninja/fact")
        return res.json()

class AnalyzeCats(Resource):
    def get(self):
        res = requests.get("https://catfact.ninja/fact")
        return toolbox.analyze_text(res.json()["fact"])

class Analyze(Resource):
    def post(self):
        body = request.get_json(silent=True) or {}
        try:
            return toolbox.analyze_text(body.get("text"))
        except ValueError as err:
            return {"error": str(err)}, 400


class Convert(Resource):
    def get(self):
        try:
            return toolbox.convert_temperature(
                request.args.get("value"), request.args.get("unit")
            )
        except ValueError as err:
            return {"error": str(err)}, 400

class Dice(Resource):
    def get(self):
        try:
            return toolbox.roll_dice(
                request.args.get("sides", 6), request.args.get("count", 1)
            )
        except ValueError as err:
            return {"error": str(err)}, 400


class Todo(Resource):
    """/api/todos - the whole list"""
    """/api/todos/<int:item_id> - specific items"""

    def get(self):
        return todos.all()

    def post(self):
        body = request.get_json(silent=True) or {}
        try:
            return todos.add(body.get("title")), 201  # 201 = Created
        except ValueError as err:
            return {"error": str(err)}, 400

    def put(self, item_id):
        try:
            return todos.complete(item_id)
        except KeyError as err:
            return {"error": err.args[0]}, 404

    def delete(self, item_id):
        try:
            todos.remove(item_id)
            return "", 204  # 204 = No Content
        except KeyError as err:
            return {"error": err.args[0]}, 404

# Routes
api.add_resource(Analyze, "/api/analyze")
api.add_resource(Convert, "/api/convert")
api.add_resource(Dice, "/api/dice")
api.add_resource(Todo, "/api/todos", "/api/todos/<int:item_id>")
api.add_resource(AnalyzeCats, "/api/cats", "/api/cats/analyze")

if __name__ == "__main__":
    app.run(debug=True)

