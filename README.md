# Проект YaCut

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
- обязательного для длинной исходной ссылки;
- необязательного для пользовательского варианта короткой ссылки.
Пользовательский вариант короткой ссылки не должен превышать 16 символов.

Проект запускается командой из корневой директории:
```sh
flask run
```
## Пример работы сервиса:
- Длинная ссылка
https://practicum.yandex.ru/trainer/backend-developer/lesson/12e07d96-31f3-449f-abcf-e468b6a39061/
- Короткая ссылка
http://yacut.ru/lesson

Также доступно API проекта по эндпоинтам:
- /api/id/ — POST-запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

## Пример API запросов
#### endpoint: http://127.0.0.1:5000/api/id/
- method: POST
- body:
> {
    "url": "https://github.com/mortodello/yacut/blob/master/html/index.html",
    "custom_id": "CglCAZgg"
}
- response:
> {
    "short_link": "http://localhost/CglCAZgg",
    "url": "https://github.com/mortodello/yacut/blob/master/html/index.html"
}

#### endpoint: http://127.0.0.1:5000/api/id/CglCAZgg/
- method: GET
- response:
> {
    "url": "https://github.com/mortodello/yacut/blob/master/html/index.html"
}

Проект написан с применением FLASK, Python
Автор Корсаков Сергей [mortodello](https://github.com/mortodello/yacut/blob/master/html/index.html)

