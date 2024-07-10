## Дипломный проект. Задание 2: API-тестирование

### Автотесты для проверки API сайта Stellar Burgers https://stellarburgers.nomoreparties.site/

Реализованы проверки ручек:
* `POST /api/auth/register` - создание/регистрация пользователя
* `POST /api/auth/login` - авторизация пользователя
* `PATCH /api/auth/user` - получение и обновление информации о пользователе
* `POST /api/orders` - cоздание заказа
* `GET /api/orders` - получение заказов пользователя

### Структура проекта

- `tests` - пакет с тестами заданных ручек
- `conftest.py` - файл с фикстурами
- `api.py` - файл с методами, вызываемыми в ходе тестов
- `data.py` - файл URLs и другими данные для тестов
- `generators.py` - файл с вспомогательными функциями
- `README.md` - описание проекта
- `requirements` - файл с внешними зависимостями


**Установка зависимостей**

> `pip install -r requirements.txt`

**Запуск автотестов и создание отчета о тестировании в Allure**

> `pytest --alluredir=allure_results`

**Генерация отчета в html страницу**

>`allure serve allure_results`
