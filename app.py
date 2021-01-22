import json
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from login import LoginForm, SignupForm


app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'secrtidsfjo222'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://elice:miniproject2@localhost:3306/elice"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

db.create_all()
db.session.commit()

error_msgs = {
  "duplicate_user":"Username Exist. Try <a href='/login'>Sign in</a>.",
  "user_not_exist":"User does not exist. Please <a href='/signup'>sign up</a> first.",
  "wrong_password":"Invalid password. Try <a href='/login'>sign in</a> again."
}


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@app.route('/') 
def index():
  return render_template('index.html')

@app.route('/todo-personal') 
def todo_personal():
  return render_template('todo_personal.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  if form.validate_on_submit():
    exist_user = User.query.filter(User.username == form.username.data).first()
    if exist_user is not None:
      error = "duplicate_user"
      return error_msgs[error]
    else:
      hashed_pw = generate_password_hash(form.password.data, method='sha256')
      new_user = User(username = form.username.data, email = form.email.data, password = hashed_pw)
      db.session.add(new_user)
      db.session.commit()
      return redirect(url_for('login'))
  return render_template('signup_tp.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter(User.username == form.username.data).first()
    if user is None:
      error = "user_not_exist"
      return error_msgs[error]
    elif not check_password_hash(user.password, form.password.data):
      error = "wrong_password"
      return error_msgs[error]
    else:
      login_user(user, remember=form.remember_me.data)
      return redirect(url_for('dashboard'))
  return render_template('login_tp.html', form=form)

@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
  return render_template('dash_tp.html', name = current_user.username)

@app.route('/calendar')
def calendar():
    return render_template("calendar.html")

@app.route('/data')
def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')

    with open("events.json", "r") as input_data:
        return input_data.read()
# @app.route('/calendar')
# def hello():
#     return render_template("/calendar/calendar.html")


if __name__=="__main__":
  app.run(debug=True)
