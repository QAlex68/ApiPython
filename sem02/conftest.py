import pytest
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata.get("username")


@pytest.fixture()
def x_selector1():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture()
def x_selector2():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture()
def x_selector3():
    return '//*[@id="app"]/main/div/div/div[2]/h2'


@pytest.fixture()
def btn_selector():
    return 'button'


@pytest.fixture()
def er1():
    return '401'


@pytest.fixture()
def x_selector4():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'


@pytest.fixture()
def er2():
    return 'Hello, {}'.format(name)
