from flask import Blueprint, render_template
from todaypoopoo.forms.user_form import UserLoginForm, UserCreateForm


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup')
def signup():
    form = UserCreateForm()
    return render_template('auth/signup.html', form=form)