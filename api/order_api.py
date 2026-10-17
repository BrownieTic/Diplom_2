import requests
import allure

from urls import API as api

class OrderAPI:
    def create_order_request(self, ingredient_id, token):
        with allure.step("Отправка запроса на оформление заказа"):
            response = requests.post(api.create_order_api, json = {"ingredients": ingredient_id}, headers = {'Authorization': token})
        return response

    def create_order_request_without_login(self, ingredient_id):
        with allure.step("Отправка запроса на оформление заказа без регистрации"):
            response = requests.post(api.create_order_api, json = {"ingredients": ingredient_id})
        return response
    