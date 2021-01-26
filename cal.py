from flask import Blueprint
from flask import render_template, redirect, url_for, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required
from form import LoginForm, SignupForm
from db import User, db

bp = Blueprint("calendar", __name__, url_prefix="/calendar")

@bp.route('/calendar', methods=['GET', 'POST'])
def signup():
    return render_template('calendar.html')
