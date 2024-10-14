import time
import yaml
from module import Site

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

site = Site(testdata['address'])
name = testdata.get('username')
passwd = testdata.get('password')
post_title = testdata.get('post_title')
post_description = testdata.get('post_description')
post_content = testdata.get('post_content')


# css_selector = 'span.mdc-text-field__ripple'
# print(site.get_element_property('css', css_selector, 'height'))
#
# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property('xpath', xpath, 'color'))

def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, er1):
    input1 = site.find_element('xpath', x_selector1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_selector)
    btn.click()
    err_label = site.find_element('xpath', x_selector3)
    text = err_label.text
    assert text == er1


def test_step2(x_selector1, x_selector2, x_selector4, btn_selector, er2):
    input1 = site.find_element('xpath', x_selector1)
    input1.clear()
    input1.send_keys(name)
    input2 = site.find_element('xpath', x_selector2)
    input2.clear()
    input2.send_keys(passwd)
    btn = site.find_element('css', btn_selector)
    btn.click()
    err_label = site.find_element('xpath', x_selector4)
    text = err_label.text
    # site.quit()
    assert text == er2


def test_add_post(x_selector1, x_selector2, btn_selector, create_btn, post_title_input, post_description_input,
                  post_content_input, post_save_btn, post_title_selector):
    # Жмем на кнопку создания поста
    create_post_btn = site.find_element('css', create_btn)
    create_post_btn.click()
    time.sleep(testdata['wait'])

    # Вводим данные поста
    title_input = site.find_element('xpath', post_title_input)
    title_input.send_keys(post_title)
    description_input = site.find_element('xpath', post_description_input)
    description_input.send_keys(post_description)
    content_input = site.find_element('xpath', post_content_input)
    content_input.send_keys(post_content)
    time.sleep(testdata['wait'])

    # Жмем на кнопку сохраняем пост
    time.sleep(testdata['wait'])
    save_btn = (site.find_element('css', post_save_btn))
    save_btn.click()
    time.sleep(testdata['wait'])

    # Проверяем, что новый пост появился с заданным названием
    post_title_element = site.find_element('xpath', post_title_selector)
    assert post_title_element.text == post_title


if __name__ == '__main__':
    pass
