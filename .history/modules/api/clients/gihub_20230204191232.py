import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body


  """   def get_user_defunkt(self):
        # r = requests.get("https://api.github.com/users/defunkt")
        r = requests.get("https://api.github.com/users/octocat")
        body = r.json()

        return body

    def get_non_exist_user(self):
        r = requests.get("https://api.github.com/users/burlakasergii")
        body = r.json()

        return body """
