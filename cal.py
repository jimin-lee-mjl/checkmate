import json
from db import TodoList, db
from flask import Flask, json, request, jsonify, app
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
from flask import current_app
from flask import Blueprint
from flask import render_template, redirect, url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required
from form import LoginForm, SignupForm
from db import TodoListCal, db
import sys

bp = Blueprint("calendar", __name__, url_prefix="/calendar")

@bp.route('/personal')
def calendar():
    return render_template("calendar.html")

# @bp.route('/elice')
# def calendar():
#     return render_template("calendar.html")

# @bp.route('/study')
# def calendar():
#     return render_template("calendar.html")


@bp.route('/datacal')
# def get_data():
#     result = TodoListCal.query.filter(TodoListCal.id== 1).all()
#     return str(result)

# def make_json():
#     with open('events.json','w') as outfile:
#         json.dump(get_data(),outfile,indent=4)

def get_todo_cal():
    todoListCal = TodoListCal.query.all()
    a = []
    for todoList in todoListCal:
        hi = {
        "title":todoList.title,
        "start": todoList.start,
        "end":todoList.end
        }
        a.append((hi))
    print(json.dumps(a), file=sys.stdout)
    return json.dumps(a)