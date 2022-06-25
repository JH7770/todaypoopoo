from flask import Blueprint, render_template, request, flash, g, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from todaypoopoo import db
from todaypoopoo.forms import UserLoginForm, UserCreateForm
from todaypoopoo.models import User

from sqlalchemy import or_

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/signup',  methods=['GET', 'POST'])
def signup():
    form = UserCreateForm()
    if request.method =='GET':
        return render_template('auth/signup.html', form=form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter(
            User.userid == form.userid.data,
        ).first()

        if user :
            flash('이미 존재하는 아이디입니다.')
            return render_template('auth/signup.html', form=form)

        user = User(
            userid=form.userid.data,
            username=form.username.data,
            password=generate_password_hash(form.password1.data),
            email=form.email.data
        )

        db.session.add(user)
        db.session.commit()
        return render_template('auth/signup_success.html')

    return render_template('auth/signup.html', form=form)

@bp.route('/login',  methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if request.method =='GET':
        return render_template('auth/login.html', form=form)

    elif request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(userid=form.userid.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."

        if error:
            flash(error)
        else:
            session.clear()
            session['user_id'] = user.id
            _next = request.args.get('next', '')
            if _next:
                return redirect(_next)
            else:
                return redirect(url_for('main.index'))

    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))