from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

from .constants import SHORT_MAX_LENGTH


class YacutForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, SHORT_MAX_LENGTH), Optional()]
    )
    submit = SubmitField('Создать')