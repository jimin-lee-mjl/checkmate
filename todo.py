from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from db import db, TodoList

bp = Blueprint('todo', __name__, url_prefix='/todo')
api = Api(bp)

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('content')

class Personal(Resource):
    def get(self):
        result = []
        query = TodoList.query.all()
        for todo in query:
            result.append({'title':todo.title, 'content':todo.content, 'due':todo.due, 'status':todo.status})
        return jsonify(status = 'success', result=result)

    def post(self):
        args = parser.parse_args()
        new_todo = TodoList()
        new_todo.title = args['title']
        new_todo.content = args['content']
        # login required 적용하고 new_todo.user_id = current_user.id 추가하기 
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(status = 'success', result = {'title':new_todo.title, 'content':new_todo.content})


api.add_resource(Personal, '/personal')