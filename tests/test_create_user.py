import allure
import json
import pytest

from api.create_user_api import CreateUserAPI
from data import UserData as data

@allure.feature("")
class TestCreatUser:
    def test_create_uniq_new_user(self, request):
        response = request.create_user_request(data.USER)
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            assert 'accessToken' in response.json()

    def test_create_user_duplicate(self, create_user_and_delete):
        response = create_user_and_delete.create_user_request(data.USER)
        r = response.json()
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 403
            assert r["success"] == "false"
            assert r["message"] == "User already exists"
