import logging
from testpaga_api import api_get_posts, api_create_post, api_get_user_posts
import yaml

with open("./testdata.yaml") as f:
    data = yaml.safe_load(f)


def test_get_posts(login, testtext1):
    logging.info("Test 0-1 API Starting")
    res = api_get_posts(login)
    assert res is not None
    assert res.status_code == 200
    titles = [post["title"] for post in res.json()["data"]]
    assert testtext1 in titles


def test_create_post(login, post_data):
    logging.info("Test 0-2 API Starting")
    res = api_create_post(login, post_data)
    assert res is not None
    assert res.status_code == 200


def test_get_user_posts(login, created_post):
    logging.info("Test 0-3 API Starting")
    res = api_get_user_posts(login)
    assert res is not None
    assert res.status_code == 200
    descriptions = [post["description"] for post in res.json()["data"]]
    assert created_post["description"] in descriptions





    #
    # # Проверка поста с определенным заголовком (из лекции)
    # def test_step1(login, testtext1):
    #     header = {"X-Auth-Token": login}
    #     res = requests.get(data["address"] + "api/posts", params={"owner": "notMe"}, headers=header)
    #     listres = [i["title"] for i in res.json()["data"]]
    #     assert testtext1 in listres
    #
    #
    # # Проверка создание нового поста
    # def test_step2(login, post_data):
    #     header = {"X-Auth-Token": login}
    #     res = requests.post(data["address"] + "api/posts", headers=header, data=post_data)
    #     assert res.status_code == 200
    #
    #
    # # Проверка наличия моего поста по его описанию
    # def test_step3(login, created_post):
    #     header = {"X-Auth-Token": login}
    #     res = requests.get(data["address"] + "api/posts", params={"owner": "me"}, headers=header)
    #     descriptions = [i["description"] for i in res.json()["data"]]
    #     assert created_post["description"] in descriptions
