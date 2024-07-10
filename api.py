import allure
import requests
from data import URLs


class UsersAPI:
    def __init__(self):
        self.main_url = URLs.MAIN_URL
        self.url_user_create = f'{URLs.MAIN_URL}{URLs.ENDPOINT_USER_CREATE}'
        self.url_user_login = f'{URLs.MAIN_URL}{URLs.ENDPOINT_USER_LOGIN}'
        self.url_user_update = f'{URLs.MAIN_URL}{URLs.ENDPOINT_USER_UPDATE}'
        self.url_user_delete = f'{URLs.MAIN_URL}{URLs.ENDPOINT_USER_DELETE}'

    @allure.step('Создать пользователя')
    def create_new_user(self, payload):
        response = requests.post(self.url_user_create, data=payload)
        return response

    @allure.step('Авторизовать пользователя')
    def auth_login_user(self, payload):
        response = requests.post(self.url_user_login, data=payload)
        return response

    @allure.step('Обновить данные о пользователе')
    def update_user_data(self, token_user, payload):
        headers = {"Authorization": token_user}
        response = requests.patch(self.url_user_update, headers=headers, data=payload)
        return response

    @allure.step('Удалить пользователя')
    def delete_user(self, token_user):
        headers = {"Authorization": token_user}
        response = requests.delete(self.url_user_delete, headers=headers)
        return response

class OrdersAPI:
    def __init__(self):
        self.main_url = URLs.MAIN_URL
        self.url_order = f'{URLs.MAIN_URL}{URLs.ENDPOINT_ORDER_CREATE}'

    @allure.step('Создать новый заказ')
    def create_new_order(self, token_user, ingredients_data):
        headers = {'Authorization': token_user}
        payload = {'ingredients': ingredients_data}
        response = requests.post(self.url_order, headers=headers, json=payload)
        return response

    @allure.step('Получить список заказов пользователя')
    def get_user_orders(self, token_user):
        headers = {"Authorization": token_user}
        response = requests.get(self.url_order, headers=headers)
        return response

