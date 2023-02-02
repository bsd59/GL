import pytest
import requests
# import io

# @pytest.mark.http
# def test_first_request():
#     r = requests.get('https://api.github.com/zen')
#     print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    # r = rr.json('utf-8')
    # print(f"Response is {r.text}")
    # print(r)
    # print(rr.json('utf-8'))

    # print(f"Response Body is {r.json()}")
    # r = requests.get('https://api.github.com/users/defunkt')
    # print(f"Response Body is {r.json()}")

    # print(f"Response Status code is {r.status_code}")
    # print(f"Response Headers are {r.headers}")
    
    # print(r.text.encode("utf-8")) ###
    # print(f"Response is {r.text.encode('utf-8')}") ### ok
