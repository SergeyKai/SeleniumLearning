import requests

key = ''
url = 'https://sms-activation-service.com/stubs/handler_api'


def get_status(number_id: int):
    params = {
        'api_key': key,
        'action': 'getStatus',
        'id': number_id,
        'lang': 'ru',

    }

    response = requests.get(
        url,
        params=params
    )

    response_message = response.text.split(':')

    if response_message[0] == 'STATUS_OK':
        return response_message[1]
    else:
        return False


def get_number():
    params = {
        'api_key': key,
        'action': 'getNumber',
        'service': 'ot',
        'operator': 'any',
        'country': '0',
        'lang': 'ru',
    }
    response = requests.get(
        url=url,
        params=params
    )
    print(response.text)

    response_message = response.text.split(':')
    if response_message[0] == 'ACCESS_NUMBER':
        return {
            'id': response_message[1],
            'number': response_message[2]
        }
    else:
        return response.text


if __name__ == '__main__':
    get_number()
