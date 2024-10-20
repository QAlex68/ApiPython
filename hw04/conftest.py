import pytest, yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('./testdata.yaml') as f:
    data = yaml.safe_load(f)
    browser = data['browser']


@pytest.fixture(scope='session')
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


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

# import pytest
# import yaml
#
# with open("./testdata.yaml") as f:
#     testdata = yaml.safe_load(f)
# name = testdata.get('username')
#
#
# @pytest.fixture()
# def x_selector1():
#     return '//*[@id="login"]/div[1]/label/input'
#
#
# @pytest.fixture()
# def x_selector2():
#     return '//*[@id="login"]/div[2]/label/input'
#
#
# @pytest.fixture()
# def x_selector3():
#     return '//*[@id="app"]/main/div/div/div[2]/h2'
#
#
# @pytest.fixture()
# def btn_selector():
#     return 'button'
#
#
# @pytest.fixture()
# def er1():
#     return '401'
#
#
# @pytest.fixture()
# def x_selector4():
#     return '//*[@id="app"]/main/nav/ul/li[3]/a'
#
#
# @pytest.fixture()
# def er2():
#     return 'Hello, {}'.format(name)
#
#
# @pytest.fixture()
# def create_btn():
#     return '#create-btn'
#
#
# @pytest.fixture()
# def post_title_input():
#     return '//*[@id="create-item"]/div/div/div[1]/div/label/input'
#
#
# @pytest.fixture()
# def post_description_input():
#     return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'
#
#
# @pytest.fixture()
# def post_content_input():
#     return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'
#
#
# @pytest.fixture()
# def post_save_btn():
#     return 'button[type="submit"]'
#
#
# @pytest.fixture()
# def post_title_selector():
#     return '//*[@id="app"]/main/div/div[1]/h1'
