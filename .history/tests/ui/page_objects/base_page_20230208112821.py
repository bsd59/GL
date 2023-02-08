from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# клас BasePage базові операції роботи з браузером;
# -проініціалізувати драйвер
# -закрити браузер
class BasePage:
    PATH = r