import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# модуль для пошуку елементів за певними атрибутами
from selenium.webdriver.common.by import By

# додамо затримку для тесту
import time


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
    # метод send_keys -операцыя введення тексту до елемента сторінки
    login_elem.send_keys("sergiiburlaka@mistakeinemail.com")

    # Знаходимо поле, в яке введемо хибний пароль
    # це беремо з DevTools: id="password"
    login_elem = driver.find_element(By.ID, "password")

    # Bведемо хибний пароль
    # метод send_keys -операцыя введення тексту до елемента сторінки
    login_elem.send_keys("wrong password")

    # Знаходимо кнопку Sing in
    # це беремо з DevTools: name="commit"
    bnt_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою миші
    # метод click() -операцыя натискання лівої кнопки миші на елементі
    bnt_elem.click()

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    # title -aтрибут, який зберігає заголовок сторінки
    assert driver.title == "Sign in to GitHub · GitHub"

    # даєм затримку після тесту,
    # зробимо паузу на 3 секунди, щоб побачити вікно браузера
    # по команді $ pytest -m ui в вікні Git Bush
    time.sleep(3)

    # Закриваємо браузер
    driver.close()
