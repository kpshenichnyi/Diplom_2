import allure
from faker import Faker
import secrets


@allure.step('Сгенерировать данные для регистрации нового пользователя')
def generate_new_user():
    fake_user = Faker(locale="ru_RU")
    data_user = {
        'email': fake_user.email(),
        'password': fake_user.password(),
        'name': fake_user.name()
    }
    return data_user

@allure.step('Сгенерировать рандомный хэш для ошибочных ингредиентов')
def generate_random_hex_24():
    hex = secrets.token_hex(12)
    return hex
