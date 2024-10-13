import pytest
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture
def good_word():
    return 'Привет'


@pytest.fixture
def bad_word():
    return 'Првет'
