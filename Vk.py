from urllib.parse import urlencode
from pprint import pprint

import requests

APP_ID = 7490139
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status',
    'response_type': 'token',
    'v': '5.52'
}

TOKEN = '7370e3a5db05f0795fef94b584fa9c4c0b53537a09592f30b3b31f1255d42b00a080ced3a66ef2e44f0dd'
TOKEN2 = 'cac8b520abee0fc12fd7ab519d452c261bd8cdc0220238a4ac8a80012db60a7dc4647d81dcbf329dd60f0'

class User:

    def __init__(self, token):
        self.token = token


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
        pass

    def __str__(self):
        return "https://vk.com/id{}".format()

    friends = None


user1 = User(TOKEN)
user2 = User(TOKEN2)
user2.friends = user2.get_friends()
pprint(user2.friends)
#print(user1 & user2)