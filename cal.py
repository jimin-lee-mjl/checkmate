import json
from db import TodoList, db
from db import Category, db
from flask import Flask, json, request, jsonify, app
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
from flask import current_app
from flask import Blueprint
from flask import render_template, redirect, url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required
from form import LoginForm, SignupForm
import sys
bp = Blueprint("calendar", __name__, url_prefix="/calendar")

@bp.route('/')
def calendar():
    return render_template("calendar.html")

@bp.route('/datacal')
#@login_required
def get_todo_cal():
    todoListCal = TodoList.query.all()
    a = []
    is_important = ''
    color = ''
    for todoList in todoListCal:
        if todoList.status==0 and todoList.important == 1:
            is_important = "important"
        else:
            is_important = ''

        hi = {
        "title":todoList.content,
        "start": todoList.start_date,
        "end":todoList.end_date,
        "important": is_important,
        "color" : todoList.category.color
        }
        a.append((hi))
    #print(json.dumps(a), file=sys.stdout)
    return json.dumps(a)