import subprocess
import yaml, time
from testpage_ui import OperationsHelper
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

name = testdata.get('username')
passw = testdata.get('password')
post_title = testdata.get('post_title')
post_description = testdata.get('post_description')
post_content = testdata.get('post_content')
your_name = testdata.get('your_name')
your_email = testdata.get('your_email')
your_content = testdata.get('your_content')


def test_step1(browser):
    logging.info('Test 1-1 UI Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_step2(browser):
    logging.info("Test 1-2 UI Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passw)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"


# ДЗ02

def test_add_post(browser):
    logging.info("Test 1-3 UI Starting")
    testpage = OperationsHelper(browser)
    testpage.click_create_post_button()
    testpage.input_title_post(post_title)
    testpage.input_description_post(post_description)
    testpage.input_content_post(post_content)
    testpage.click_save_post_button()
    time.sleep(2)
    assert testpage.get_new_title_text() == post_title


# ДЗ03

def test_step4(browser):
    logging.info("Test 1-4 UI Starting")
    testpage = OperationsHelper(browser)
    testpage.click_create_contact()
    testpage.enter_your_name(your_name)
    testpage.enter_your_email(your_email)
    testpage.enter_your_content(your_content)
    testpage.click_submit_contact()
    time.sleep(3)
    assert testpage.get_alert_text() == "Form successfully submitted"


# Не знаю насколько это рационально, я вызвал как из командной строки посредством subprocess.run, но работает
# def test_report():
#     logging.info("Отчет отправлен qalex68@mail.ru")
#     subprocess.run(["python", "mail.py"])


if __name__ == '__main__':
    pass
