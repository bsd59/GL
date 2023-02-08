# модуль містить клас для взаємодії з сторінкою
# імпорт модулів з створеної базової сторінки та з Selenium
from modules.ui.page_objcts.sign_in_page import SignInPage
import pytest


def test_check_incorrect_username_page_object():
    # створення обєкту сторінки 
    sign_in_page = SignInPage()
    
    # адресу сторінки зберігати у відповідному їй класі
  
    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # задаємо атрибут для адреси сторінки:


    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check driver.title == "Sign in to GitHub · GitHub"

