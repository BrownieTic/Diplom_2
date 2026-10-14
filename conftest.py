import pytest
import json

from api.create_user_api import CreateUserAPI
from data import UserData as data

@pytest.fixture(scope="function")
def request():
    request = CreateUserAPI()
    return request

@pytest.fixture(scope="function")
def delete_user(request):
    yield request
    token = request.json()["accessToken"]
    request.delete_user_request(token)

@pytest.fixture(scope="function")
def create_user_and_delete(request):
    response = request.create_user_request(data.USER)
    token = response.json()["accessToken"]
    yield request
    request.delete_user_request(token)
