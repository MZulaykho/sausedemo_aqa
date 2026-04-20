from config.base_url import URL
from pages.base_page import BasePage


def test_tc_sauce_001(page):
    base_page = BasePage(page)
    base_page.open_page(URL)
    base_page.validate_url(URL)