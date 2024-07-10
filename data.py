class URLs:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    ENDPOINT_USER_CREATE = '/api/auth/register'
    ENDPOINT_USER_LOGIN = '/api/auth/login'
    ENDPOINT_USER_UPDATE = '/api/auth/user'
    ENDPOINT_USER_DELETE = '/api/auth/user'
    ENDPOINT_ORDER_CREATE = '/api/orders'
    ENDPOINT_GET_INGREDIENTS = '/api/ingredients'
    ENDPOINT_GET_USER_ORDERS = '/api/orders'


class DefaultUserData:

    default_user = {'email': 'itpetry@ya.ru',
                    'password': '1@qwerty&9',
                    'name': 'itpetry'}

class BurgerIngredients:
    burger_without_ingredients = []

    # Бургер только с булкой, name = '"Краторная булка N-200i"'
    # burger_with_one_ingredient = { 'name': "Краторная булка N-200i",
    #                                     'ingredients': ["61c0c5a71d1f82001bdaaa6c"]}
    burger_with_one_ingredient = "61c0c5a71d1f82001bdaaa6c"
    burger_with_one_ingredient_name = "Краторный бургер"

    # 'Фалленианский люминесцентный антарианский краторный бургер'
    burger_with_all_ingredients = { 'name': "Фалленианский люминесцентный антарианский краторный бургер",
                                         'ingredients': ["61c0c5a71d1f82001bdaaa75", "61c0c5a71d1f82001bdaaa6e",
                                                            "61c0c5a71d1f82001bdaaa77", "61c0c5a71d1f82001bdaaa6c"]}
