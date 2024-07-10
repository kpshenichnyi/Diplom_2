import allure
import pytest
import generators
from api import UsersAPI


@allure.description('Тесты на Создание\Регистрацию пользователя')
class TestUserCreate:
    @allure.title('Проверить успешное создание уникального пользователя с корректными данными')
    def test_create_uniq_user_response_success(self, fix_create_user, fix_delete_user):
        response = fix_create_user[1]

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверить ошибку при создании НЕ уникального пользователя (уже существующего)')
    def test_create_not_uniq_user_response_failed(self, fix_create_user):
        data_registered_user = fix_create_user[0]
        response = UsersAPI().create_new_user(data_registered_user)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title('Проверить ошибки при создании пользователя, без заполненных Email\Password\Имя')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_with_empty_fields_response_failed(self, field):
        user_data = generators.generate_new_user()
        user_data.pop(field)
        response = UsersAPI().create_new_user(user_data)

        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
