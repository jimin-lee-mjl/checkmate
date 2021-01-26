from flask import Blueprint
from flask import render_template, redirect, url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required
from form import LoginForm, SignupForm
from db import User, db

bp = Blueprint("auth", __name__, url_prefix="/auth")

login_manager = LoginManager()
login_manager.init_app(current_app)
login_manager.login_view = 'auth.login'


error_msgs = {
    "duplicate_user":"Username already exists. Try <a href='/auth/login'>Sign in</a>.",
    "duplicate_email":"Email already exists. Try <a href='/auth/signup'>sign up</a> with a different email.",
    "user_not_exist":"User does not exist. Please <a href='/auth/signup'>sign up</a> first.",
    "wrong_password":"Invalid password. Try <a href='/auth/login'>sign in</a> again."
  }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        exist_username = User.query.filter(User.username == form.username.data).first()
        exist_email = User.query.filter(User.email == form.email.data).first()
        if exist_username:
            error = "duplicate_user"
            return error_msgs[error]
        elif exist_email:
            error = "duplicate_email"
            return error_msgs[error]
        else:
            hashed_pw = generate_password_hash(form.password.data, method='sha256')
            new_user = User(username = form.username.data, email = form.email.data, password = hashed_pw)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
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
    return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))