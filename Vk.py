from urllib.parse import urlencode
from pprint import pprint
import json

import requests

APP_ID = 7490365
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status',
    'response_type': 'token',
    'v': '5.52'
}

TOKEN = 'c67b8de203d401deeea696fd415c28fd2af1c9022f18a6c13d294c0fa866c065dd0c13ab5dacad3878139'
TOKEN2 = 'eec04b1980aafb5d1ff96463af0ea1fd169dbf32cc15a7fd69ee950b416087f6820b28996cc13ee788dbd'


class User:

    def __init__(self, token):
        self.token = token

    friends = None

    def get_friends(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': self.token,
                'v': 5.103
            }
        )

        return response.json()

    def get_joint_friends(self, friend_id):
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params={
                'access_token': self.token,
                'target_uid': friend_id,
                'v': 5.103
            }
        )

        return response.json()

    def __and__(self, other):
        return list(set(self.friends) & set(other.friends))


#    def __str__(self):
#        return "https://vk.com/id{}".format()


user1 = User(TOKEN)
user1.friends = user1.get_friends()["response"]["items"]

user2 = User(TOKEN2)
user2.friends = user2.get_friends()["response"]["items"]

pprint(user1 & user2)
