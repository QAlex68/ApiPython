import yaml
from module import Site

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


site = Site(testdata['address'])
name = testdata.get('username')
passwd = testdata.get('password')


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
    site.quit()
    assert text == er2


if __name__ == '__main__':
    pass
