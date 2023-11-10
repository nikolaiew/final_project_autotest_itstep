import pytest
import random
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_login()
        page.is_button_feedback()  # hover
        page.is_button_delivery()  # hover
        page.is_button_warranty()  # hover
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
        page.is_samsung()
        page.is_samsung_j701()

    def test_main_page_content(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_main_slider()
        page.is_cat_zaryadky()
        page.is_cat_power_banks()  # hover
        page.is_info_block_vozvrat()
        page.is_info_block_dostavka()
        page.is_info_block_otsrochka()
        page.is_info_block_podderzhka()
        page.is_show_all_new_prod()
        page.is_show_all_new_prod_left()
        page.is_show_all_new_prod_right()
        page.is_section_new_products()
        page.is_new_product_8()
        page.is_button_show_hits()
        page.is_button_prev_hits()
        page.is_button_next_hits()
        page.is_section_hits()
        page.is_button_prev_trends()
        page.is_button_next_trends()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_logo_footer()
        page.is_button_subscribe()

    def test_main_page_subscribe_actions(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.subscribe_actions(self.email_for_subscribe)
        page.is_alert_success_after_subscribe()
