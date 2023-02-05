import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'
# https://api.github.com/users/defunkt  # perevirka v brouseri


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('burlakasergii')
    assert r['message'] == 'Not Found'
# https://api.github.com/users/burlakasergii  # perevirka v brouseri


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 26
# https://api.github.com/search/repositories?q=become-qa-auto # perevirka v brouseri
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiiburlaka_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
# https://api.github.com/search/repositories?q=s # perevirka v brouseri


""" from modules.api.clients.gihub import GitHub
@pytest.mark.api
def test_user_exists():
    api = GitHub()
    user = api.get_user_defunkt()
    assert user["login"] == "octocat"
@pytest.mark.api
def test_user_not_exists():
    api = GitHub()
    r = api.get_non_exist_user()
    assert r["message"] == "Not Found" """
