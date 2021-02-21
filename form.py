from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField(
        'username', 
        validators=[InputRequired(), Length(min=4, max=15, message="유저네임은 4자 이상 15자 이하입니다.")]
    )
    password = PasswordField(
        'password', 
        validators=[InputRequired(), Length(min=8, max=80, message="비밀번호는 8자 이상입니다.")]
    )

class SignupForm(FlaskForm):
    username = StringField(
        'username', 
        validators=[InputRequired(), Length(min=4, max=15, message="유저네임은 4자 이상 15자 이하입니다.")]
    )
    email = StringField(
        'email', 
        validators=[
            InputRequired(), 
            Email(message='이메일 형식이 유효하지 않습니다.'), 
            Length(max=50, message="이메일은 50자 이하입니다.")
        ]
    )
    password = PasswordField(
        'password', 
        validators=[InputRequired(), Length(min=8, max=80, message="비밀번호는 8자 이상입니다.")]
    )