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

#데이터베이스에서 데이터 읽어와서 json파일에 저장
@bp.route('/datacal')
def get_data():
  result = TodoListCal.query.filter(TodoListCal.id== 1).all()
  return str(result)

def make_json():
  with open('test.json', 'w') as outfile:
    json.dump(get_data(), outfile, indent=4)




