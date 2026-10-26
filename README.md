
# Home_work_Pro — Books and Categories REST API

Учебный проект на Django REST Framework.

Проект реализует REST API для управления книгами и категориями.
Выполнен в рамках сложного домашнего задания (Home_work_Pro).

## Возможности

### Книги
- GET — получение списка книг и отдельной книги.
- POST — создание новой книги.
- PUT — полное обновление книги.
- PATCH — частичное обновление книги.
- DELETE — удаление книги.

### Категории
- GET — получение списка категорий.
- POST — создание новой категории.
- GET — получение отдельной категории.
- PUT — полное обновление категории.
- PATCH — частичное обновление категории.
- DELETE — удаление категории.

### Связь между моделями
- Добавлена модель Category.
- В модели Book используется ForeignKey на Category.
- Одна категория может содержать несколько книг.
- Используется related_name="books".
- Реализован вложенный сериализатор CategoryDetailSerializer.
- Для получения вложенных книг используется prefetch_related('books').

## Используемые технологии

- Python
- Django
- Django REST Framework
- drf-spectacular
- SQLite

## Установка и запуск

1. Создать и активировать виртуальное окружение.

2. Установить зависимости:

   pip install -r requirements.txt

3. Применить миграции:

   python manage.py migrate

4. Запустить сервер:

   python manage.py runserver

## Документация Swagger

После запуска сервера открыть:

http://127.0.0.1:8000/api/docs/

## Основные API-эндпоинты

### Книги
- GET /api/books/
- POST /api/books/
- GET /api/books/{id}/
- PUT /api/books/{id}/
- PATCH /api/books/{id}/
- DELETE /api/books/{id}/

### Категории
- GET /api/categories/
- POST /api/categories/
- GET /api/categories/{id}/
- PUT /api/categories/{id}/
- PATCH /api/categories/{id}/
- DELETE /api/categories/{id}/

### Категория с вложенными книгами
- GET /api/categories/{id}/detail/

Этот эндпоинт возвращает информацию о категории
и список всех книг, относящихся к ней.

## Пример вложенного ответа

{
  "id": 2,
  "name": "Фантастика",
  "description": "Фантастическая литература",
  "books": [
    {
      "id": 3,
      "title": "451 градус по Фаренгейту",
      "author": "Рэй Брэдбери",
      "published_date": "1953-10-19",
      "isbn": "9781451673319",
      "page_count": 256,
      "cover": "",
      "category": 2
    }
  ]
}

## Тестирование

API проверено через Swagger UI и Django REST Framework.

- Создание книги: HTTP 201 Created.
- Получение категории с вложенными книгами: HTTP 200 OK.
- Проверена связь Book и Category.
- Проверено отображение нового эндпоинта в Swagger.

Примечание: локальная база данных db.sqlite3 не включена
в репозиторий. После установки проекта категории и книги
необходимо создать самостоятельно через API.
