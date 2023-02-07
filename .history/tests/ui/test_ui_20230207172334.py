import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення обєкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r'c:\QA\RepoHP\GL' + r'\chromedriver.exe')
    )

    # Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Закриваємо браузер
    driver.close()