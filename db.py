from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from config import DB_CONNECT

current_app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{DB_CONNECT['username']}:{DB_CONNECT['password']}@{DB_CONNECT['server']}:3306/{DB_CONNECT['dbname']}"
current_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(current_app)


class User(UserMixin, db.Model):
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(15), unique=True, nullable=False)
      email = db.Column(db.String(50), unique=True, nullable=False)
      password = db.Column(db.String(80), nullable=False)

class Category(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(45), unique=True, nullable=False)
      color = db.Column(db.String(45), default='navy')
      user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)

class TodoListCal(UserMixin, db.Model):
      id = db.Column(db.Integer, primary_key=True)
      title = db.Column(db.String(20), nullable=False)
      start = db.Column(db.String(20), nullable=False)
      end = db.Column(db.String(20))
      important = db.Column(db.Boolean, default=False)
      color = db.Column(db.String(20))


class TodoList(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      content = db.Column(db.Text, default="To do something")
      start_date = db.Column(db.DateTime, default=db.func.now())
      end_date = db.Column(db.DateTime, nullable=True)
      status = db.Column(db.Boolean, default=False)
      important = db.Column(db.Boolean, default=False)
      user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
      category_id = db.Column(db.Integer, default=1)
# status -> doing:false(0), done:true(1)

def init_db():
      #db.drop_all()
      db.create_all()
      # sample_category = Category(name="mine")
      # sample_todo = TodoList(content="elice")
      # db.session.add(sample_category)
      # db.session.add(sample_todo)
      db.session.commit()
