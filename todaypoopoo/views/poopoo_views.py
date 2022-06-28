from datetime import datetime, date, timedelta
from flask import Blueprint, request, render_template, redirect, url_for, flash, g
from sqlalchemy import and_, func


from todaypoopoo.models import PooPoo, User
from todaypoopoo.forms import PooPooRecordForm
from todaypoopoo import db

bp = Blueprint('poopoo', __name__, url_prefix='/poopoo')

@bp.route('/main', methods=['GET', 'POST'])
def main():
    form = PooPooRecordForm()
    yesterday = date.today() - timedelta(days=1)
    poopoo_yesterday = len(PooPoo.query.filter(and_(PooPoo.user_id == g.user.userid, func.date(PooPoo.date) == yesterday)).all())
    poopoo_today = len(PooPoo.query.filter(and_(PooPoo.user_id == g.user.userid, func.date(PooPoo.date) == date.today())).all())
    print(poopoo_today, poopoo_yesterday)
    if request.method == 'GET' and g.user:
        return render_template('poopoo/main.html', form=form, success=False, poopoo_yesterday=poopoo_yesterday,
                               poopoo_today=poopoo_today)

    if request.method == 'POST' and form.validate_on_submit():
        poopoo = PooPoo(date=datetime.now(), user_id=form.userid.data)
        db.session.add(poopoo)
        db.session.commit()
        return render_template('poopoo/main.html', form=form, success=True, poopoo_yesterday=poopoo_yesterday,
                               poopoo_today=poopoo_today + 1)
    return flash('error')


@bp.route('/calendar')
def calendar():
    return render_template('poopoo/calendar.html')