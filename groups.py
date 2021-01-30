from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from db import db, Group, Member, User

bp = Blueprint('groups', __name__, url_prefix='/groups')
api = Api(bp)

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('username')
parser.add_argument('role')

class Caegories(Resource):
    def get(self):
        result = []
        query = Category.query.all()
        for g in query:
            result.append({'id':g.id, 'name':g.name})
        return jsonify(status = 'success', result = result)

    def post(self):
        args = parser.parse_args()
        new_group = Group()
        new_group.name = args['name']
        db.session.add(new_group)
        db.session.commit()
        return jsonify(status = 'success', result = {'id':new_group.id, 'name':new_group.name})

    def put(self):
        args = parser.parse_args()
        the_group = Group.query.filter_by(id = args['id']).first()
        the_group.name = args['name']
        db.session.commit()
        return jsonify(status = 'success', result = {'id':the_group.id, 'name':the_group.name})

    def delete(self):
        args = parser.parse_args()
        the_group = Group.query.filter_by(id = args['id']).first()
        db.session.delete(the_group)
        db.session.commit()
        return jsonify(status = 'success', result = {'id':the_group.id, 'name':the_group.name})

class Members(Resource):
    def get(self, group_id):
        result = []
        query = db.session.query(Member).filter_by(group_id = group_id).all()
        for m in query:
            user = User.query.filter_by(id = m.user_id).first()
            result.append({'username':user.username})
        return jsonify(status = 'success', result = {'member_list':result, 'total':len(result)})

    def post(self, group_id):
        args = parser.parse_args()
        find_group = Group.query.filter_by(id = group_id).first()
        find_user = User.query.filter_by(username = args['username']).first()
        if find_user:
            find_group.members.append(find_user)
            db.session.commit()
        else:
            msg = 'User does not exist. Check the username again.'
            return jsonify(result = {'error_msg':msg})
        return jsonify(status = 'success', result = {'name':find_user.username})

api.add_resource(Groups, '/')
api.add_resource(Members, '/<group_id>')