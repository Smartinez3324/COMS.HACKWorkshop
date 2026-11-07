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

class Cat(Resource):
    def get(self):
        return {"Hello"}     

api.add_resource(Cat, "/api/cats")


if __name__ == "__main__":
    app.run(debug=True)


