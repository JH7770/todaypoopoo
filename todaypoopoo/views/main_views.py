from flask import Blueprint, render_template, g
from todaypoopoo.forms.user_form import UserLoginForm
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    form = UserLoginForm()
    return render_template('main.html', form=form)

@bp.route('/calendar')
def calendar():
    return render_template('calendar.html')