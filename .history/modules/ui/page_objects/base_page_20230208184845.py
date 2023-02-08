from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# клас BasePage реалізує базові операції роботи з браузером:
class BasePage:
    # поля класу для ініціалізації драйвера
    PATH = 'C:\QA\RepoHP\GL\'
    DRIVER_NAME = 'chromedriver.exe'

    # -проініціалізувати драйвер
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    # -закрити браузер
    def close(self):
        self.driver.close()
