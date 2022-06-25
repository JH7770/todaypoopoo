from datetime import datetime
from flask import Blueprint, request, render_template, redirect, url_for, flash

from todaypoopoo.models import PooPoo
from todaypoopoo.forms import PooPooRecordForm
from todaypoopoo import db

bp = Blueprint('poopoo', __name__, url_prefix='/poopoo')

@bp.route('/record', methods=['GET', 'POST'])
def record():
    form = PooPooRecordForm()
    if request.method == 'GET':
        return render_template('poopoo/main.html', form=form, success=False)

    if request.method == 'POST' and form.validate_on_submit():
        poopoo = PooPoo(date=datetime.now(), user_id=form.userid.data)
        db.session.add(poopoo)
        db.session.commit()
        return render_template('poopoo/main.html', form=form, success=True)
    return flash('error')