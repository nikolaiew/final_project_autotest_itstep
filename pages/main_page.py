from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):

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

    def is_samsung_j701(self):
        assert self.hover_actions(*locators.BasePageLocators.SAMSUNG), \
            "Button 'Samsung' is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_J701), \
            "Button 'Samsung J701' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

