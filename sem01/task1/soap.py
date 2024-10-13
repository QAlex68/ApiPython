from zeep import Client, Settings
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

wsdl = data['wsdl']
# wsdl = 'https://speller.yandex.net/services/spellservice?WSDL'
settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def checkText(text):
    response = client.service.checkText(text)
    return response[0]['s']


if __name__ == '__main__':
    checkText('Превет')
