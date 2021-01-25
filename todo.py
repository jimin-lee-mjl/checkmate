from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from db import db, TodoList

bp = Blueprint('todo', __name__, url_prefix='/todo')
api = Api(bp)

class Personal(Resource):
    def get(self):
        result = []
        query = TodoList.query.all()
        for todo in query:
            result.append({'title':todo.title, 'content':todo.content, 'due':todo.due, 'status':todo.status})
        return jsonify(status = 'success', result=result)


api.add_resource(Personal, '/personal')