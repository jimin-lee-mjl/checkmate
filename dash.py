import json
import sys
from db import TodoList, db
from flask import jsonify,Blueprint, render_template
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
from flask_login import login_required
from datetime import datetime

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")



def get_today_todo(): 
    todoListCal = TodoList.query.all()
    today_date = datetime.now().strftime("%Y%m%d")
    a = []
    for todoList in todoListCal:
        start_date = str(todoList.start_date).replace('-','')
        end_date = todoList.end_date
        if todoList.status==0 and start_date <= today_date:
            if end_date == None or today_date <= str(end_date).replace('-',''):
                hi = {
                "title":todoList.content,
                "start": todoList.start_date,
                "end":todoList.end_date
                }
                a.append((hi))
    return a

def get_progress():
    todoListCal = TodoList.query.all()
    today_date = datetime.now().strftime("%Y%m%d")
    a = []
    doing = 0
    done = 0
    for todoList in todoListCal:
        start_date = str(todoList.start_date).replace('-','')
        end_date = todoList.end_date
        if start_date <= today_date:
            if end_date == None or today_date <= str(end_date).replace('-',''):
                doing+=1
                if todoList.status==1: 
                    done += 1
    hi = {
            "done": done,
            "doing": doing,
            "progress":done/doing*100
        }
    a.append((hi))
    return a


def get_important_todo():
    todoListCal = TodoList.query.all()
    a = []
    for todoList in todoListCal:
        if todoList.status==0 and todoList.important == 1:
            hi = {
            "title":todoList.content,
            "start": todoList.start_date,
            "end":todoList.end_date
            }
            a.append((hi))
    return a


def get_upcoming_todo(): 
    today_date = datetime.now().strftime("%Y%m%d")
    todoListCal = TodoList.query.all()
    a = []
    for todoList in todoListCal:
        end_date = str(todoList.end_date).replace('-','')
        if todoList.status == 0 and end_date == today_date:
            hi = {
            "title":todoList.content,
            "start": todoList.start_date,
            "end":todoList.end_date
            }
            a.append((hi))
    return a



@bp.route('/')
@login_required
def print_dashboard():
    important_list = get_important_todo()
    upcoming_list = get_upcoming_todo()
    today_list = get_today_todo()
    progress = get_progress()
    return render_template("dashboard.html",today_list= today_list,important_list = important_list,upcoming_list =upcoming_list,progress=progress)
