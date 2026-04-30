from config.base_url import URL
from config.users import LOGIN, PASSWORD
from pages.login_page import LoginPage


def test_tc_sauce_001(page):
    login_page = LoginPage(page)
    login_page.open_page(URL)
    login_page.validate_url(URL)

    login_page.fill_user_name(LOGIN)
    value = "standard_user"
    login_page.expect_user_name(value)

    login_page.fill_password(PASSWORD)
    value = "secret_sauce"
    login_page.expect_password(value)

    login_page.click_button_login()
