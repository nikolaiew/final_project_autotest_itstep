from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, '//div[@class="top_bar_user"]/a[@href="user/login"]')
    DETAILS = (By.XPATH, '//a[text()="Детали сотрудничества"]')
    FEEDBACK = (By.XPATH, '//a[@href="singlepage/feedback"]')
    DELIVERY = (By.XPATH, '//a[@href="singlepage/delivery"]')
    WARRANTY = (By.XPATH, '//a[@href="singlepage/warranty"]')
    PHONE = (By.XPATH, '//div[text()="+38 098 911 95 22"]')
    CURRENCY = (By.XPATH, '//select[@id="currency"]')
    UAH = (By.XPATH, '//option[@class="custom_list clc"]')
    USD = (By.XPATH, '//option[@value="USD"]')
    EUR = (By.XPATH, '//option[@value="EUR"]')
    LOGO_HEADER = (By.XPATH, '//img[@src="images/logo.png"]')
    SEARCH_INPUT = (By.XPATH, '//input[@id="typeahead"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    WISH_BUTTON = (By.XPATH, '//a[@href="wish/show"]')
    CART_BUTTON = (By.XPATH, '//a[@href="cart/show"]')
    NEW_BUTTON = (By.XPATH, '//div[@class="links-for-checks"]/a[1]')
    DISCOUNTS_BUTTON = (By.XPATH, '//div[@class="links-for-checks"]/a[2]')
    HITS_BUTTON = (By.XPATH, '//div[@class="links-for-checks"]/a[3]')
    SAMSUNG = (By.XPATH, '//li[6]/div')
    SAMSUNG_J701 = (By.XPATH, '//li[6]/ul/li[55]')

    SUBSCRIBE = (By.XPATH, '//button[@class="newsletter_button"]')
    SUBSCRIBE_INPUT = (By.XPATH, '//input[@type="email"]')
    ALERT_SUCCESS = (By.XPATH, "//div[@id = 'alert-success']")
    LOGO_FOOTER = (By.XPATH, '//img[@src="images/logo-footer.png"]')


class MainPageLocators:
    MAIN_SLIDER = (By.XPATH, '//div[@class = "screen_slider"]')
    CAT_ZARYADKY = (By.XPATH, '//a[@href="category/zaryadki"]')
    CAT_POWER_BANKS = (By.XPATH, '//a[@href="category/paver-bank-power-bank"]')

    VOZVRAT_SREDSTV = (By.XPATH, '//div[@class="characteristics"]/div/div/div[1]')
    BESPLATNAYA_DOSTAVKA = (By.XPATH, '//div[@class="characteristics"]/div/div/div[2]')
    OTSROCHKA_OPLATY = (By.XPATH, '//div[@class="characteristics"]/div/div/div[3]')
    TEH_PODDERZHKA = (By.XPATH, '//div[@class="characteristics"]/div/div/div[4]')

    SHOW_ALL_NEW_BUTTON = (By.XPATH, '//a[@href="main/showNew"][text()="Показать все"]')
    SHOW_ALL_NEW_LEFT_BUTTON = (By.XPATH, '//div[@class="arrivals_nav_container"]/div[1]/i')
    SHOW_ALL_NEW_RIGHT_BUTTON = (By.XPATH, '//div[@class="arrivals_nav_container"]/div[2]/i')
    NOVYE_POSTUPLENIYA_PANEL = (By.XPATH, '//div[@class="product_panel panel active"]')
    NOVYE_POSTUPLENIYA_8 = (By.XPATH, '//div[@class="product_panel panel active"]//div[3]/div[2]')

    SHOW_ALL_HITS_BUTTON = (By.XPATH, '//a[@href="main/showHit"][text()="Показать все"]')
    SHOW_ALL_HITS_LEFT_BUTTON = (By.XPATH, '//div[@class="best_nav_container"]/div[1]/i')
    SHOW_ALL_HITS_RIGHT_BUTTON = (By.XPATH, '//div[@class="best_nav_container"]/div[2]/i')
    HITY_PRODAZH_PANEL = (By.XPATH, '//div[@class="bestsellers_panel panel active"]')
    HITY_PRODAZH_C2_R2 = (By.XPATH, '//div[@class="bestsellers_panel panel active"]//div[@class="slick-slide slick-active"][1]/div[2]')

    TRENDY_LEFT_BUTTON = (By.XPATH, '//div[@class="trends_slider_nav"]/div[1]')
    TRENDY_RIGHT_BUTTON = (By.XPATH, '//div[@class="trends_slider_nav"]/div[2]')
    TRENDY_C2 = (By.XPATH, '//div[@class="col-lg-9"]//div[@class="slick-slide slick-active"][1]')

