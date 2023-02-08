# модуль містить клас для взаємодії з сторінкою
# імпорт модулів з створеної базової сторінки та з Selenium
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


# клас SignInPage наслідує клас BasePage
class SignInPage(BasePage):
    # у підході PageObject прийнято
    # адресу сторінки зберігати у відповідному їй класі
    # задаємо атрибут для адреси сторінки:
    URL = 'https://github.com/login'

    # конструктор класу який
    # викликає- super(). конструктор базового класу- __init__()
    # в якому ініціалізується драйвер для комунікації з браузером
    def __init__(self) -> None:
        super().__init__()

    # метод обєкту для відкриття сторінки
    def go_to(self):
        # атрибут класу SignInPage.URL зберігає адресу сторінки
        self.driver.get(SignInPage.URL)
