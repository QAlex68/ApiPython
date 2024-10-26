import subprocess
import yaml, time
from testpage_ui import OperationsHelper
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata.get('username')
passw = testdata.get('password')
# post_title = testdata.get('post_title')
# post_description = testdata.get('post_description')
# post_content = testdata.get('post_content')
# your_name = testdata.get('your_name')
# your_email = testdata.get('your_email')
# your_content = testdata.get('your_content')


def test_step1(browser):
    logging.info('Test 1-1 UI Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_step2(browser):
    logging.info('Test 1-2 UI Starting')
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passw)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"

def test_step3(browser):
    logging.info('Test 1-4 UI Starting')
    testpage = OperationsHelper(browser)
    testpage.click_about()
    time.sleep(3)
    assert testpage.get_about_text() == ("About Page")
    assert testpage.get_about_property() == "32px"


if __name__ == '__main__':
    pass
