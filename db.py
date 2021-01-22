from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

current_app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://elice:miniproject2@localhost:3306/elice"
db = SQLAlchemy(current_app)

class User(UserMixin, db.Model):
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(15), unique=True, nullable=False)
      email = db.Column(db.String(50), unique=True, nullable=False)
      password = db.Column(db.String(80), nullable=False)

def init_db():
    db.create_all()
    db.session.commit()
