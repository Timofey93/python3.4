import requests
from pprint import pprint


AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
VERSION = '5.65'
APP_ID = 6124391

auth_data = {
    'client_id': APP_ID,
    'response_type': 'token',
    'scope': 'friends, status, video',
    'v': VERSION,
}
token = 'cc2bb672d462acd37a8deb4a9db9677ed67115c6ea2c284dccd7ccb4a6a3a1a751c8f38f2b74c54721aa6'

def get_my_friends():

    params = {
        'access_token': token,
        'v': VERSION,
        'user_id': '',
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    all_my_friends = response.json()['response']['items']
    return all_my_friends


def get_fiends_from_friends():

    friends_list = list()
    for i in get_my_friends():
        params = {
            'access_token': token,
            'v': VERSION,
            'user_id': i,
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        friends_list.extend(response.json()['response']['items'])
        return friends_list


def get_same_friends():
    same_friends = set(get_my_friends()) & set(get_fiends_from_friends())

    print('Общие друзья - ', same_friends)

get_same_friends()
