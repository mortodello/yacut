from flask import jsonify, request
from http import HTTPStatus

from . import app, db
from .constants import SHORT_MAX_LENGTH, URL
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .validators import validate_symbols
from .views import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_link(short_id):
    link = URLMap.query.filter_by(short=short_id).first()
    if not link:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': link.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def post_link():
    try:
        data = request.get_json()
    except Exception:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_unique_short_id(data['url'])
    validate_symbols(data['custom_id'])
    if len(data['custom_id']) > SHORT_MAX_LENGTH:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.')
    link = URLMap(original=data['url'], short=data['custom_id'])
    db.session.add(link)
    db.session.commit()
    return jsonify({'url': link.original,
                    'short_link': URL + link.short}), HTTPStatus.CREATED
