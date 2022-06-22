from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('main.html')

@bp.route('/calendar')
def calendar():
    return render_template('calendar.html')