from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class UserCreateForm(FlaskForm):
    userid = StringField('사용자아이디', validators=[DataRequired('이름을 입력하세요.'), Length(min=3, max=25, message='아이디는 3자 이상 25자 이하여야 합니다.')])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    username = StringField('사용자이름', validators=[DataRequired('이름을 입력하세요.'), Length(min=3, max=25, message='아이디는 3자 이상 25자 이하여야 합니다.')])

    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])