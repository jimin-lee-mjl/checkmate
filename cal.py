import jsonify
from sqlalchemy import text
from flask import Blueprint
from flask import render_template, redirect, url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required
from form import LoginForm, SignupForm
from db import TodoList, db


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

#데이터베이스에서 데이터 읽어와서 파일에 저장
@bp.route('/data')
def get_data():
  sql = text('select * from todo')
  result = TodoList.query.filter(db.session.execute(sql)).all()
  #nrow = len(result)
  #return jsonify(result) 
  #return statement.compile(result)


