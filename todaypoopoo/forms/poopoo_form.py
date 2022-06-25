from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class PooPooRecordForm(FlaskForm):
    userid = StringField('사용자 아이디', validators=[DataRequired(), Length(min=3, max=25)])
