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

    # метод обєкту для відкриття-.get сторінки
    # через драйвер- .driver , який ініціалізований
    # в базовому класі- BasePage
    def go_to(self):
        # атрибут класу SignInPage.URL зберігає адресу сторінки
        # через self. ініціалізує драйвер для комунікації з браузером
        self.driver.get(SignInPage.URL)

    # метод задача якого ввести імя та пароль
    # та натиснути кнопку Sing in
    def try_login(self, username, password)
    # Знаходимо поле, в яке введемо хибне ім'я користувача або поштову адресу
    # за іменем атрибута- ID ,та його значенням,
    # це беремо з DevTools: id="login_field"
    # метод find_element -операція пошуку елемента
    login_elem = self.driver.find_element(By.ID, "login_field")

    # Bведемо хибне ім'я користувача або поштову адресу
    # метод send_keys -операцыя введення тексту до елемента сторінки
    login_elem.send_keys(username)

    # Знаходимо поле, в яке введемо хибний пароль
    # це беремо з DevTools: id="password"
    pass_elem = self.driver.find_element(By.ID, "password")

    # Bведемо хибний пароль
    # метод send_keys -операцыя введення тексту до елемента сторінки
    pass_elem.send_keys(password)

    # Знаходимо кнопку Sing in
    # це беремо з DevTools: name="commit"
    bnt_elem = self.driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою миші
    # метод click() -операцыя натискання лівої кнопки миші на елементі
    bnt_elem.click()


    def check_title(self, expected_title):
        return self.driver.title == expected_title
