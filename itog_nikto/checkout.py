import subprocess
import requests
import yaml
import logging

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_token():
    path_1 = data.get('address_users')
    post = requests.post(url=path_1, data={'username': data.get('login'), 'password': data.get('password')})
    if post.status_code == 200:
        return post.json()['token']
    else:
        logging.error(f'Ошибка авторизации, код ошибки {post.status_code}. Неверные пароль, логин. ')
        return None


def get_user(token, id):
    path_2 = f'{data.get("address_api")}/{id}'
    get = requests.get(url=path_2, headers={'X-Auth-Token': token})
    if get.status_code == 200:
        res = get.json()['firstName']
        logging.info(f'Получено имя пользователя {res}')
        return res
    else:
        logging.error(f'Kод ошибки {get.status_code}. Неверные пароль, логин. ')
        return None


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    return False


def getout(cmd):
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout