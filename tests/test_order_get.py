import allure
import pytest
import generators
from api import UsersAPI, OrdersAPI


@allure.description('Тесты на Получение Списка Заказов')
class TestOrdersGet:
    @allure.title('Получить список заказов авторизованного пользователя')
    def test_get_orders_with_authorized_user_response_success(self):
        authorized_user_data = {"email": "itpetry@ya.ru", "password": "1@qwerty&9", "name": "itpetry"}
        authorized_response = UsersAPI().auth_login_user(authorized_user_data)
        token_user = authorized_response.json().get('accessToken', '')
        get_response = OrdersAPI().get_user_orders(token_user)

        assert get_response.status_code == 200
        assert get_response.json()['success'] is True

    @allure.title('Получить список заказов для неавторизованного пользователя')
    def test_get_orders_unauthorized_user_response_failed(self):
        authorized_user_data = {}
        token_user = 'None'
        get_response = OrdersAPI().get_user_orders(token_user)

        assert get_response.status_code == 401
        assert get_response.json().get('message') == "You should be authorised"