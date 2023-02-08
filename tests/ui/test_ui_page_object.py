# модуль містить клас для взаємодії з сторінкою
# імпорт модулів з створеної базової сторінки та з Selenium
from modules.ui.page_objects.sign_in_page import SignInPage
import pytest

# маркуємо тест: ui -група тестів
@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення обєкту сторінки для взаємодії з нею
    sign_in_page = SignInPage()

    # адресу сторінки зберігати у відповідному їй класі

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # спроба увійти в систему GitHub
    sign_in_page.try_login(
        "sergiiburlaka@mistakeinemail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # закриваємо браузер
    sign_in_page.close()
