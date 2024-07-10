import allure
import pytest
import generators
from api import UsersAPI


@allure.description('Тесты на Изменение данных пользователя')
class TestUserUpdate:
    @allure.title('Проверить изменение данных у авторизованного пользователя')
    @pytest.mark.parametrize("update_to_field, new_value_to_field", [("name", "new_name_for_user"),
                                                                ("email", "new_email_for_user@ya.ru"),
                                                                ("password", "new_password_user")])
    def test_update_user_with_auth_response_success(self, fix_auth_user, update_to_field, new_value_to_field):
        updated_data_for_user = {update_to_field: new_value_to_field}
        token_user = fix_auth_user[2]
        response = UsersAPI().update_user_data(token_user, updated_data_for_user)

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверить изменение данных пользователя без авторизации')
    @pytest.mark.parametrize("update_to_field, new_value_to_field", [("name", "new_name_for_user"),
                                                                ("email", "new_email_for_user@ya.ru"),
                                                                ("password", "new_password_user")])
    def test_update_user_without_auth_response_failed(self, update_to_field, new_value_to_field):
        updated_data_for_user = {update_to_field: new_value_to_field}
        token_user = 'None'
        response = UsersAPI().update_user_data(token_user, updated_data_for_user)

        assert response.status_code == 401
        assert response.json()['message'] == "You should be authorised"
