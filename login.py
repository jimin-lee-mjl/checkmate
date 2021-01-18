from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import UserMixin

# flask-wtf, flask-bootstrap, (email_validator), flask-login

users = []

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember_me = BooleanField('remember me')

class SignupForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class User(UserMixin):
    def __init__(self, username, email, password):
        self.id = len(users) + 1
        self.username = username
        self.email = email
        self.password = password
    def create_user(self):
        users.append(self)

user1 = User('elice', 'elice@elice.com', 'rabbithole')
user1.create_user()