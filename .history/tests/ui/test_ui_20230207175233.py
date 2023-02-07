import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# модуль для пошуку елементів за певними атрибутами
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення обєкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r'c:\QA\RepoHP\GL' + r'\chromedriver.exe')
    )

    # Відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле, в яке введемо хибне ім'я користувача або поштову адресу
    # метод find_element -операцыя пошуку елемента 
    # за іменем атрибута- ID ,та його значенням, 
    # це беремо з DevTools: id="login_field"
    login_elem = driver.find_element(By.ID, "login_field")

    # Bведемо хибне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiiburlaka@mistakeinemail.com")

    # Закриваємо браузер
    driver.close()
