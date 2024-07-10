import allure
import pytest
import generators
from api import UsersAPI


@allure.description('Тесты на Авторизацию пользователя')
class TestUserAuthLogin:
    @allure.title('Проверить успешную авторизацию пользователя, с корректными данными')
    def test_auth_user_correct_data_response_success(self, fix_auth_user):
        response = fix_auth_user[1]

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверить невозможности авторизации пользователя с некорректным логином')
    def test_auth_user_with_incorrect_login_response_failed(self):
        data_user = generators.generate_new_user()
        response = UsersAPI().auth_login_user(data_user)

        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'

    @allure.title('Проверить невозможности авторизации пользователя с некорректным паролем')
    def test_auth_user_with_incorrect_password_response_failed(self):
        data_user = {'email': 'itpetry@ya.ru', 'password': '12345', 'name': 'itpetry'}
        response = UsersAPI().auth_login_user(data_user)

        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'


