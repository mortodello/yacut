from flask import flash, redirect, render_template

from random import randrange

from . import app, db
from .constants import SHORT_LINK_SYMBOLS, SHORT_MIN_LEHGTH, RANGE_FOR_RANDOM
from .forms import YacutForm
from .models import URLMap


def get_unique_short_id(link):
    result = ''
    for i in range(SHORT_MIN_LEHGTH):
        result += chr(SHORT_LINK_SYMBOLS[randrange(RANGE_FOR_RANDOM)])
    if URLMap.query.filter_by(short=result).first() is not None:
        result = '' + get_unique_short_id(link)
    return result


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = YacutForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short:
            short = get_unique_short_id(form.original_link.data)
        if URLMap.query.filter_by(short=short).first() is not None:
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)
        link = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(link)
        db.session.commit()
        return render_template('index.html', form=form, link=link)
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def link_view(short):
    link = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(link.original)
