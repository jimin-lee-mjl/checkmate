import json
from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_bootstrap import Bootstrap
from flask_login import login_required, current_user

def create_app():
  app = Flask(__name__)

  bootstrap = Bootstrap(app)
  app.config['SECRET_KEY'] = 'secrtidsfjo222'

  @app.route('/') 
  def index():
    return render_template('tasks.html')

  @app.route('/tasks') 
  def tasks():
    return render_template('tasks.html')

  @app.route('/tasks-group') 
  def tasks_group():
    return render_template('tasks_group.html')

  @app.route('/dashboard')
  @login_required
  def dashboard():
    return render_template('dash_tp.html', name = current_user.username)


  @app.route('/data')
  def return_data():
      start_date = request.args.get('start', '')
      end_date = request.args.get('end', '')

      with open("events.json", "r") as input_data:
          return input_data.read()
  

  with app.app_context():
    import db
    db.init_db()

    import auth
    app.register_blueprint(auth.bp)

    import todo
    app.register_blueprint(todo.bp)

    import groups
    app.register_blueprint(groups.bp)

    import cal
    app.register_blueprint(cal.bp)


  if __name__=="__main__":
    app.run(debug=True)  

  return app

    

