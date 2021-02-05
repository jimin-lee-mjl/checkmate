import json
import sys
from flask import Flask, render_template, redirect, url_for, jsonify, request, flash
from flask_bootstrap import Bootstrap
from flask_login import login_required, current_user
from config import SECRET_KEY

app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/') 
@login_required
def dashboard():
  return render_template('dashboard.html')

@app.route('/tasks') 
@login_required
def tasks():
  return render_template('tasks.html')

@app.route('/calendar/data')
def return_data():
  return cal.get_todo_cal()


with app.app_context():
  import db
  db.init_db()

  import auth
  app.register_blueprint(auth.bp)

  import todo
  app.register_blueprint(todo.bp)

  import cal
  app.register_blueprint(cal.bp)

  import dash
  app.register_blueprint(dash.bp)

if __name__=="__main__":
  app.run(debug=True) 
    

