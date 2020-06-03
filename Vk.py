from urllib.parse import urlencode
from pprint import pprint
import requests

APP_ID = 7497406
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.52'
}

TOKEN = 'c38edc1d1df4ac74d2dbe21635494221219418efbc16581bf5c0c278123bdfb345465693e1dd12e253645'
TOKEN2 = '7a2c81acba1f21dd4cd60d511f7605f1068826bb663e0222f18e7910e80f9a161631a2a54b11331b0241f'


class User:

    def __init__(self, token):
        self.token = token

    def __and__(self, other):
        return list(set(self.friends) & set(other.friends))

    def __str__(self):
        return "https://vk.com/id{}".format(self.id)

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

    def get_user(self):
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': self.token,
                'v': 5.103
            }
        )
        return response.json()

    id = None
    friends = None


user1 = User(TOKEN)
user1.friends = user1.get_friends()["response"]["items"]
user1.id = user1.get_user()["response"][0]["id"]

user2 = User(TOKEN2)
user2.friends = user2.get_friends()["response"]["items"]
user2.id = user2.get_user()["response"][0]["id"]

pprint(user1 & user2)
print(user1, user2)
