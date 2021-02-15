from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from config import DB_CONNECT
from sqlalchemy.orm import relationship
from datetime import date

current_app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{DB_CONNECT['username']}:{DB_CONNECT['password']}@{DB_CONNECT['server']}:3306/{DB_CONNECT['dbname']}"
current_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(current_app)


class User(UserMixin, db.Model):
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(15), unique=True, nullable=False)
      email = db.Column(db.String(50), unique=True, nullable=False)
      password = db.Column(db.String(80))

class Category(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(45), nullable=False)
      color = db.Column(db.String(45))
      user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)

class TodoList(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      content = db.Column(db.Text, default="To do something")
      start_date = db.Column(db.Date, default=db.func.now())
      end_date = db.Column(db.Date, nullable=True)
      status = db.Column(db.Boolean, default=False)
      important = db.Column(db.Boolean, default=False)
      user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
      category_id = db.Column(db.Integer,db.ForeignKey(Category.id), default=1)
      category = relationship("Category")
# status -> doing:false(0), done:true(1)

def init_db():
      db.init_app(current_app)
      db.drop_all()
      db.create_all()
      sample_user = User(username="lana", email="lana@lana.com", password=generate_password_hash('lanalana', method='sha256'))
      db.session.add(sample_user)
      db.session.commit()
      sample_category = Category(name="mine", user_id=1)
      sample_category2 = Category(name="hola", user_id=1)
      db.session.add(sample_category)
      db.session.add(sample_category2)
      db.session.commit()
      sample_todo = TodoList(content="task1", user_id=1, category_id=1)
      sample_todo2 = TodoList(content="task2", user_id=1, category_id=2)
      db.session.add(sample_todo)
      db.session.add(sample_todo2)
      db.session.commit()
