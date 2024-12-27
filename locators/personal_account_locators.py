from selenium.webdriver.common.by import By


class PersonalAccountLocators:

    STELLAR_LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a')
    PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account"]')  # Кнопка "Личный кабинет"
    LOGIN_ACC = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    ORDER_HISTORY = (By.XPATH, '//a[@href="/account/order-history"]') #История заказов
    ORDER_LIST = (By.XPATH, '//ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]')
    ORDERS_ID_IN_HISTORY = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]/a/div[1]/p[1]')

    LOGOUT_BTN = (By.XPATH, '//button[contains(text(), "Выход")]') #Кнопка ВЫХОД
    PROFILE_PAGE_DESCRIPTION = (By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]') # Текст с описанием в левом углу профиля
    ORDERS_LST = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]') #заказы