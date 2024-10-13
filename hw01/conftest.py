import pytest
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    res = requests.post(data["address"] + "gateway/login",
                        data={"username": data["username"], "password": data["password"]})
    return res.json()["token"]


@pytest.fixture()
def testtext1():
    return "Заголовок поста"


@pytest.fixture()
def post_data():
    return {
        "title": "Заголовок поста",
        "description": "Какое то описание поста",
        "content": "Содержание"
    }


@pytest.fixture()
def created_post(login, post_data):
    header = {"X-Auth-Token": login}
    res = requests.post(data["address"] + "api/posts", headers=header, data=post_data)
    assert res.status_code == 200
    return post_data
