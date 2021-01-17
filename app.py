from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from login import LoginForm, SignupForm, User

#Flask 객체 인스턴스 생성
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'secrtidsfjo222'

@app.route('/') # 접속하는 url
def index():
  return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  if form.validate_on_submit():
    new_user = User(form.username.data, form.email.data, form.password.data)
    new_user.create_user()
    return new_user.user_db[0]

  return render_template('signup_tp.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    return f"hi your username is {form.username.data} and password is {form.password.data}"

  return render_template('login_tp.html', form=form)

@app.route('/dashboard')
def dashboard():
  return "login"

if __name__=="__main__":
  app.run(debug=True)