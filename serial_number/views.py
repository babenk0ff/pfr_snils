from flask import Blueprint, render_template, request, flash

from forms import CheckNumberForm
from models import SerialNumber

serial_number = Blueprint('serial_number', __name__)


@serial_number.route('/', methods=['GET', 'POST'], endpoint='index')
def check_serial_number():
    form = CheckNumberForm(request.form)

    if form.validate_on_submit():
        serial_num = form.serial_number.data
        serial_num_obj = SerialNumber.query.filter(
            SerialNumber.number == serial_num
        ).first()

        if serial_num_obj:
            flash(f'Номер {serial_num} НАЙДЕН в базе', category='success')
        else:
            flash(f'Номер {serial_num} ОТСУТСТВУЕТ в базе', category='error')

        return render_template(
            'serial_number/check.html',
            form=form,
        )

    if form.errors:
        for msg in form.errors.values():
            flash(*msg, category='error')

    return render_template(
        'serial_number/check.html',
        form=form,
    )
