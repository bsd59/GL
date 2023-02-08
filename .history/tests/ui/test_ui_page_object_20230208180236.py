# модуль містить клас для взаємодії з сторінкою
# імпорт модулів з створеної базової сторінки та з Selenium
from modules.ui.page_objcts.sign_in_page import SignInPage
import pytest


# клас SignInPage наслідує клас BasePage
class SignInPage(BasePage):
    # у підході PageObject прийнято 
    # адресу сторінки зберігати у відповідному їй класі
    # задаємо атрибут для адреси сторінки:
    URL = 'https://github.com/login'

    # конструктор класу який викликає конструктор базового класу 
    # в якому ініціалізується драйвер для комунікації з браузером
    def __init__(self) -> None:
        super().__init__()

    def

