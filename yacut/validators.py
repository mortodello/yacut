from .constants import SHORT_LINK_SYMBOLS
from .error_handlers import InvalidAPIUsage


def validate_symbols(short):
    symbols = [chr(num) for num in SHORT_LINK_SYMBOLS]
    for symbol in short:
        if symbol not in symbols:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')
