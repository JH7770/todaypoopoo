from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms_validators import AlphaNumeric

class UserCreateForm(FlaskForm):
    userid = StringField('사용자아이디',
                         validators=[DataRequired('아    이디를 입력하세요.'),
                                     Length(min=3, max=25, message='아이디는 3자 이상 25자 이하여야 합니다.'),
                                     AlphaNumeric('아이디는 영문과 숫자만 가능합니다.')
                                     ])
    email = EmailField('이메일', validators=[DataRequired('이메일을 입력하세요.'), Email()])
    username = StringField('사용자이름', validators=[DataRequired('이름을 입력하세요.'), Length(min=2, max=25, message='이름은 2자 이상 25자 이하여야 합니다.')])
    password1 = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력하세요'), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired('비밀번호 확인란을 입력하세요')])

class UserLoginForm(FlaskForm):
    userid = StringField('사용자 아이디', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])