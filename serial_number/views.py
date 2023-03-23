from typing import List

from flask import Blueprint, render_template, request, flash, redirect, \
    url_for, current_app, session
from werkzeug.utils import secure_filename

from forms import CheckNumberForm
from models import SerialNumber
from serial_number.number_checker import CheckResult, get_check_result

serial_number = Blueprint('serial_number', __name__)


@serial_number.route('/', methods=['GET', 'POST'], endpoint='check')
def check_serial_number():
    form = CheckNumberForm(request.form)
    numbers = session.pop('numbers') if 'numbers' in session.keys() else None

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
        numbers=numbers,
    )


def allowed_file(filename):
    allowed_ext = current_app.config.get('ALLOWED_EXTENSIONS')
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_ext


def read_from_file(filename):
    with open(filename, 'r') as file:
        for line in file.readlines():
            yield line.strip()


@serial_number.route('/upload', methods=['POST'], endpoint='upload')
def upload_file():
    if 'file' not in request.files:
        flash('Файл отсутствует', category='error')
        redirect(url_for('serial_number.check'))
    file = request.files['file']
    if file.filename == '':
        flash('Не был выбран файл', category='error')
        redirect(url_for('serial_number.check'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        numbers: List[CheckResult] = []
        for number in read_from_file(filename):
            numbers.append(get_check_result(number))
        session['numbers'] = numbers

        redirect(url_for('serial_number.check'))

    return redirect(url_for('serial_number.check'))
