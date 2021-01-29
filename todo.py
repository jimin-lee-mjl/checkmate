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
    #list_id에 맞춰서 가져와야 하는 것 아닌가???
    #생각해보니까... 이미 list_id로 맞춰준듯!!
    #하나의 todolist는 이미 하나의 list_id로 걸러진 것일듯!!
     
    def post(self):
        args = parser.parse_args()
        # 투두리스트를 생성하는 건 리스트 추가할 때 되고,
        # 타이틀도 디폴트로 지정되기 때문에
        # 밑에 2줄은 빼도 되지 않을까?
        new_todo = TodoList()
        new_todo.title = args['title']
        new_todo.content = args['content']
        # login required 적용하고 new_todo.user_id = current_user.id 추가하기 
        db.session.add(new_todo)
        db.session.commit()
        return jsonify(status = 'success', result = {'title':new_todo.title, 'content':new_todo.content})

    #새로운 리스트의 제목 설정이나 다름없는데 put이 restful한가?

    def put(self):
        args = parser.parse_args()
        query = TodoList.query.all()
        #일단 넣긴 넣었는데 list_id 어디서 선언해줘야 함.
        title_edited = args['title']
        for todo in query:
            todo.title = title_edited
        db.session.commit()
        return jsonify(status = 'success', result=result)

    def del(self):
        
api.add_resource(Personal, '/todo/<list_id>')
