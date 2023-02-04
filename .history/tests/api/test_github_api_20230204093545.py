import pytest

""" import sys """
""" import os """
"""  """
#""" SCRIPT_DIR = os.path.dirname(os.path.abspath(_ """_file__))
""" sys.path.append(os.path.dirname(SCRIPT_DIR)) """

from modules.api.clients.gihub import GitHub
#from modules.api.clients.gihub import GitHub

""" import requests


class GitHub:

    def get_user_defunkt(self):
        r = requests.get('https://api.github.com/users/defunkt')
        body = r.json()

        return body
 """
@pytest.mark.api
def test_user_exists():
    api = GitHub()
    user = api.get_user_defunkt()
    assert user['login'] == 'defunct'
