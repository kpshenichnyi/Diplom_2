import allure
import pytest
import generators
from api import UsersAPI


@allure.step('Создать данные пользователя, передать их, и удалить после теста')
@pytest.fixture
def fix_create_user():
    user_data = generators.generate_new_user()
    response = UsersAPI().create_new_user(user_data)
    yield user_data, response

@allure.step('Авторизоватся под пользователем и получить его токен')
@pytest.fixture
def fix_get_token_user(fix_create_user):
    data_user = fix_create_user[0]
    login_user_response = UsersAPI().auth_login_user(data_user)
    token_user = login_user_response.json()['accessToken']
    return token_user, login_user_response

@allure.step('Удалить пользователя после теста')
@pytest.fixture
def fix_delete_user(fix_get_token_user):
    yield
    UsersAPI().delete_user(fix_get_token_user[0])

@allure.step('Авторизоваться под созанным пользователем и удалить его после теста')
@pytest.fixture
def fix_auth_user(fix_create_user, fix_get_token_user, fix_delete_user):
    data_user = fix_create_user[0]
    login_user = fix_get_token_user[1]
    token_user = fix_get_token_user[0]
    yield data_user, login_user, token_user

