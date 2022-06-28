from flask import Blueprint, render_template, g, redirect, url_for
from todaypoopoo.forms.user_form import UserLoginForm
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    if g.user is None:
        return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('poopoo.main'))

