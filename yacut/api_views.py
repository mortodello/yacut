from flask import jsonify, request

from . import app, db
from .constants import SHORT_MAX_LENGTH
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .validators import validate_symbols
from .views import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_link(short_id):
    link = URLMap.query.filter_by(short=short_id).first()
    if not link:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': link.original}), 200


@app.route('/api/id/', methods=['POST'])
def add_opinion():
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
    link = URLMap()
    link.from_dict(data)
    db.session.add(link)
    db.session.commit()
    return jsonify({'url': link.original,
                    'short_link': 'http://localhost/' + link.short}), 201
