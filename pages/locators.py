from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, '//div[@class="top_bar_user"]/a[@href="user/login"]')
    FEED_BACK = (By.XPATH, '//a[@href="singlepage/feedback"]')
    DELIVERY = (By.XPATH, '//a[@href="singlepage/delivery"]')
    WARRANTY = (By.XPATH, '//a[@href="singlepage/warranty"]')
    PHONE = (By.XPATH, '//div[text()="+38 098 911 95 22"]')
    CURRENCY = (By.XPATH, '//select[@id="currency"]')
    UAH = (By.XPATH, '//option[@class="custom_list clc"]')
    USD = (By.XPATH, '//option[@value="USD"]')
    EUR = (By.XPATH, '//option[@value="EUR"]')
    LOGO = (By.XPATH, '//img[@src="images/logo.png"]')
    SEARCH_INPUT = (By.XPATH, '//input[@id="typeahead"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    WISH_BUTTON = (By.XPATH, '//a[@href="wish/show"]')
    CART_BUTTON = (By.XPATH, '//a[@href="cart/show"]')



