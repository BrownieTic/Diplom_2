import requests
import allure

from urls import API as api

class CreateUserAPI:
    def create_user_request(self, data):
        with allure.step("Отправка запроса на создание пользователя"):
            response = requests.post(api.creating_user_api, json = data)
        return response

    def delete_user_request(self, token):
        with allure.step("Отправка запроса на удаление пользователя"):
            response = requests.delete(api.delete_user_api, headers = {'Authorization': token})
        return response

class UserLoginAPI:
    def login_request(self, data):
        with allure.step("Отправка запроса на авторизацию пользователя"):
            response = requests.post(api.login_api, json = data)
        return response    