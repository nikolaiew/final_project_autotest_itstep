from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
# header
    def is_button_login(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button 'Войти' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_feedback(self):
        assert self.hover_actions(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Button 'Обратная связь' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_delivery(self):
        assert self.hover_actions(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
            "Button 'Доставка' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_warranty(self):
        assert self.hover_actions(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
            "Button 'Гарантия' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Element 'Phone number' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_currency(self):
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "Button 'Currency' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_uah(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "Button 'Currency' is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.UAH), \
            "Button 'UAH' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_eur(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "Button 'Currency' is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.EUR), \
            "Button 'EUR' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_usd(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "Button 'Currency' is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.USD), \
            "Button 'USD' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_logo_header(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_HEADER), \
            "Element LOGO HEADER is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_input(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_INPUT), \
            "Element SEARCH INPUT is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "Button SEARCH is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_wish_button(self):
        assert self.is_element_present(*locators.BasePageLocators.WISH_BUTTON), \
            "Button WISH is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cart_button(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_BUTTON), \
            "Button CART is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_new_button(self):
        assert self.is_element_present(*locators.BasePageLocators.NEW_BUTTON), \
            "Button 'Новинки' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_discounts_button(self):
        assert self.is_element_present(*locators.BasePageLocators.DISCOUNTS_BUTTON), \
            "Button 'Скидки' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_hits_button(self):
        assert self.is_element_present(*locators.BasePageLocators.HITS_BUTTON), \
            "Button 'Хиты' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_samsung(self):
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG), \
            "Button 'Samsung' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_samsung_j701(self):
        assert self.hover_actions(*locators.BasePageLocators.SAMSUNG), \
            "Button 'Samsung' is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_J701), \
            "Button 'Samsung J701' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

#content
    def is_main_slider(self):
        assert self.is_element_present(*locators.MainPageLocators.MAIN_SLIDER), \
            "Element MAIN SLIDER is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_cat_zaryadky(self):
        assert self.is_element_present(*locators.MainPageLocators.CAT_ZARYADKY), \
            "Element CAT ZARYADKY is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cat_power_banks(self):
        assert self.hover_actions(*locators.MainPageLocators.CAT_ZARYADKY), \
            "Element CAT ZARYADKY is not present or intractable"
        assert self.is_element_present(*locators.MainPageLocators.CAT_POWER_BANKS), \
            "Element CAT POWER BANKS is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_vozvrat(self):
        assert self.is_element_present(*locators.MainPageLocators.VOZVRAT_SREDSTV), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_dostavka(self):
        assert self.is_element_present(*locators.MainPageLocators.BESPLATNAYA_DOSTAVKA), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_otsrochka(self):
        assert self.is_element_present(*locators.MainPageLocators.OTSROCHKA_OPLATY), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_podderzhka(self):
        assert self.is_element_present(*locators.MainPageLocators.TEH_PODDERZHKA), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_all_new_prod(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_ALL_NEW_BUTTON), \
            "Button 'Samsung' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_all_new_prod_left(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_ALL_NEW_LEFT_BUTTON), \
            "Button 'Samsung' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_all_new_prod_right(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_ALL_NEW_RIGHT_BUTTON), \
            "Button 'Samsung' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.NOVYE_POSTUPLENIYA_PANEL), \
            "Section is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_new_product_8(self):
        assert self.is_element_present(*locators.MainPageLocators.NOVYE_POSTUPLENIYA_8), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_show_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_ALL_HITS_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_ALL_HITS_LEFT_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_ALL_HITS_RIGHT_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.HITY_PRODAZH_PANEL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_prev_trends(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDY_LEFT_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_next_trends(self):
        assert self.is_element_present(*locators.MainPageLocators.TRENDY_RIGHT_BUTTON), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

#footer
    def is_logo_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "Element LOGO FOOTER is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE), \
            "Button is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def subscribe_actions(self, email):
        assert self.input_data(*locators.BasePageLocators.SUBSCRIBE_INPUT, email), \
            "Input field is not present"
        self.explicit_wait(5)
        assert self.click_element(*locators.BasePageLocators.SUBSCRIBE), \
            "Button 'Подписаться!' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_success_after_subscribe(self):
        assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "Element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


