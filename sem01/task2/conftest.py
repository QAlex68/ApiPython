import pytest
import yaml
import requests

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    res1 = requests.post(data['address'] + 'gateway/login',
                         data={'username': data['username'], 'password': data['password']})
    # print(res1.content)
    return res1.json()['token']


@pytest.fixture()
def testtext1():
    return 'Заголовок поста'
