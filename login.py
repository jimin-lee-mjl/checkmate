from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
# flask_wtf, flask_bootstrap, (email_validator)

users = []

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])
    remember_me = BooleanField('remember me')

class SignupForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])

class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.user_db = []
    def create_user(self):
        self.user_db.append({'username':self.username, 'email':self.email, 'password':self.password})