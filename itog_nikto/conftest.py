import pytest
import string
import yaml
from datetime import datetime


with open('config.yaml') as f:
    data = yaml.safe_load(f)

@pytest.fixture(autouse=True)
def print_time():
    print(f'Start: {datetime.now().strftime("%H:%M:%S.%f")}')
    yield
    print(f'\nFinish: {datetime.now().strftime("%H:%M:%S.%f")}')
