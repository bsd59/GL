import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.mark.ui
def test_check_incorrect_username():
    # Створення обєкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r'c:\QA\RepoHP\GL' + r'\chromedriver.exe')
        )
    
    #відкриваємо сторінку 
    