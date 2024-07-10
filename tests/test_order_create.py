import allure
import pytest
from api import UsersAPI, OrdersAPI
from data import DefaultUserData, BurgerIngredients
from generators import generate_random_hex_24


@allure.description('Тесты на Создание Заказов')
class TestOrderCreate:
    @allure.title('Создать заказ с авторизацией с ингредиентом')
    def test_create_order_with_authorization_without_ingredients_success(self):
        authorized_user_data = DefaultUserData.default_user
        authorized_response = UsersAPI().auth_login_user(authorized_user_data)
        token_user = authorized_response.json().get('accessToken', '')
        ingredients_data = BurgerIngredients.burger_with_one_ingredient
        response_create = OrdersAPI().create_new_order(token_user, ingredients_data)

        assert response_create.status_code == 200
        assert response_create.json()['success'] is True
        assert response_create.json().get('name') == BurgerIngredients.burger_with_one_ingredient_name

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization_success(self):
        token_user = ''
        ingredients_data = BurgerIngredients.burger_with_one_ingredient
        response_create = OrdersAPI().create_new_order(token_user, ingredients_data)

        assert response_create.status_code == 200
        assert response_create.json().get('name') == BurgerIngredients.burger_with_one_ingredient_name

    @allure.title('Создать заказ без ингредиентов')
    def test_create_order_without_ingredients(self):
        token_user = ''
        ingredients_data = ''
        response_create = OrdersAPI().create_new_order(token_user, ingredients_data)

        assert response_create.status_code == 400
        assert response_create.json().get('message') == "Ingredient ids must be provided"

    @allure.title('Создать заказ с неверным\неизвестным хешем ингредиентов')
    def test_create_order_with_invalid_ingredients(self):
        ingredients_data = generate_random_hex_24()
        token_user = ''
        response_create = OrdersAPI().create_new_order(token_user, ingredients_data)

        assert response_create.status_code == 400
        assert response_create.text == '{"success":false,"message":"One or more ids provided are incorrect"}'

