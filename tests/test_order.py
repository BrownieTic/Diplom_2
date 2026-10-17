import allure

from data import Ingredients as ingredient

@allure.feature("Создание заказа")
class TestOrder:
    @allure.story("Успешное создание заказа")
    @allure.title("Оформление заказа с ингредиентами зарегестрированным пользователем")
    def test_order_with_login_and_ingredients_success(self, login_and_delete, request_order_class, list_id_ingredients):
        response = request_order_class.create_order_request(list_id_ingredients, login_and_delete)
        r = response.json()
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            assert r["success"] == True
            assert ingredient.INGREDIENT_BUN['name'] in r['name']
            assert ingredient.INGREDIENT_MAIN['name'] in r['name']
            assert ingredient.INGREDIENT_SAUCE['name'] in r['name']

    @allure.title("Оформление заказа без авторизации")
    def test_order_without_login_and_ingredients_success(self, request_order_class, list_id_ingredients):
        response = request_order_class.create_order_request_without_login(list_id_ingredients)
        r = response.json()
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            assert r["success"] == True
            assert ingredient.INGREDIENT_BUN['name'] in r['name']
            assert ingredient.INGREDIENT_MAIN['name'] in r['name']
            assert ingredient.INGREDIENT_SAUCE['name'] in r['name']

    @allure.title("Оформление пустого заказа зарегестрированным пользователем")
    def test_order_with_login_without_ingredients_error(self, login_and_delete, request_order_class):
        response = request_order_class.create_order_request([], login_and_delete)
        r = response.json()
        with allure.step("Проверить ошибку"):
            assert response.status_code == 400
            assert r["success"] == False
            assert r["message"] == "Ingredient ids must be provided"

    @allure.title("Оформление заказа с неверным хешом ингридиента зарегестрированным пользователем")
    def test_order_with_login_incorrect_ingredients_error(self, login_and_delete, request_order_class, list_id_ingredients):
        ingredient_id = ['643d69a5c3']
        response = request_order_class.create_order_request(ingredient_id, login_and_delete)
        r = response.json()
        with allure.step("Проверить ошибку"):
            assert response.status_code == 500    
            assert r["success"] == False    
     