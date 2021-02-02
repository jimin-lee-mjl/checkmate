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
import sys
bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")
from datetime import datetime

def get_important_todo():
    todoListCal = TodoList.query.all()
    a = []
    for todoList in todoListCal:
        if todoList.important == 1:
            hi = {
            "title":todoList.content,
            "start": todoList.start_date,
            "end":todoList.end_date,
            }
            a.append((hi))
    #b = json.dumps(a), file=sys.stdout)
    print(json.dumps(a), file=sys.stdout)
    return a


def get_urgent_todo(): 
    today_date = datetime.today().strftime("%Y-%m-%d")  
    todoListCal = TodoList.query.all()
    a = []
    for todoList in todoListCal:
        if todoList.end_date == today_date:
            hi = {
            "title":todoList.content,
            "start": todoList.start_date,
            "end":todoList.end_date,
            }
            a.append((hi))
    #b = json.dumps(a), file=sys.stdout)
    print(json.dumps(a), file=sys.stdout)
    return a

def get_today_todo(): 
    today_date = datetime.today().strftime("%Y-%m-%d")  
    todoListCal = TodoList.query.all()
    a = []
    for todoList in todoListCal:
        if todoList.start_date >= today_date and todoList.end_date >=today_date :
            hi = {
            "title":todoList.content,
            "start": todoList.start_date,
            "end":todoList.end_date,
            }
            a.append((hi))
    #b = json.dumps(a), file=sys.stdout)
    print(json.dumps(a), file=sys.stdout)
    return a


@bp.route('/')
def print_dashboard():
    important_list = get_important_todo()
    urgent_list = get_urgent_todo()
    today_list = get_today_todo()
    return render_template("dashboard.html",today_list= today_list,important_list = important_list,urgent_list =urgent_list)
