from datetime import datetime

from yacut import db
from .constants import SHORT_MAX_LENGTH


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), nullable=False)
    short = db.Column(db.String(SHORT_MAX_LENGTH),
                      unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self, data):
        if data['url']:
            setattr(self, 'original', data['url'])
        if data['custom_id']:
            setattr(self, 'short', data['custom_id'])
