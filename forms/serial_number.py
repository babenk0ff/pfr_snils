from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class CheckNumberForm(FlaskForm):
    serial_number = StringField(
        label='Поиск СНИЛС в БД',
        validators=[
            validators.DataRequired(),
            validators.Regexp(
                '^\\d{3}-\\d{3}-\\d{3} \\d{2}$',
                message='Получен неверный формат номера',
            ),
        ],
    )
    submit = SubmitField('Найти')
