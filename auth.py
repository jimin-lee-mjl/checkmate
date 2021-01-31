from flask import Blueprint, render_template, redirect, url_for, current_app, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required
from form import LoginForm, SignupForm
from db import User, db

bp = Blueprint("auth", __name__, url_prefix="/auth")

login_manager = LoginManager()
login_manager.init_app(current_app)
login_manager.login_view = 'auth.login'


error_msgs = {
    "duplicate_user":"이미 존재하는 이름입니다. 다른 이름을 사용하세요.",
    "duplicate_email":"이미 존재하는 이메일입니다. 다른 이메일을 사용하세요.",
    "user_not_exist":"존재하지 않는 이름입니다. 회원가입을 먼저 해주세요.",
    "wrong_password":"비밀번호가 틀렸습니다."
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
            flash(error_msgs['duplicate_user'], 'error')
        elif exist_email:
            flash(error_msgs['duplicate_email'], 'error')
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
    if request.method == 'POST':
        logout_user()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user is None:
                flash(error_msgs['user_not_exist'], 'error')
            elif not check_password_hash(user.password, form.password.data):
                flash(error_msgs['wrong_password'], 'error')
            else:
                login_user(user, remember=form.remember_me.data)
                return redirect(url_for('tasks'))
    return render_template('login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('tasks'))