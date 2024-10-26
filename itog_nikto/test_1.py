from checkout import checkout, get_token, get_user
import yaml
import logging

with open('config.yaml') as f:
    data = yaml.safe_load(f)


# для Ubuntu
def test_step1():
    logging.info("Test 1-1 API Starting")
    result = checkout(f"nikto -h {data['address']} -ssl -Tuning 4", "0 error(s)")
    assert result


def test_step2():
    logging.info("Test 1-2 API Starting")
    assert get_user(get_token(), '35179') == 'Pocahontas11'
