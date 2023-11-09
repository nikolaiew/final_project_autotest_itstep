import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_login()
        page.is_button_feedback()
        page.is_button_delivery()
        page.is_button_warranty()
        page.is_phone()
        page.is_button_currency()
        page.is_button_uah()
        page.is_button_usd()
        page.is_button_eur()
        page.is_logo_header()
        page.is_search_input()
        page.is_search_button()
        page.is_wish_button()
        page.is_cart_button()
        page.is_new_button()
        page.is_discounts_button()
        page.is_hits_button()
        page.is_samsung_j701()

