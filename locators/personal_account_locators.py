from selenium.webdriver.common.by import By


class PersonalAccountLocators:

    stellar_logo = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')
    personal_account = (By.XPATH, '//a[@href="/account"]')  # Кнопка "Личный кабинет"
    order_history = (By.XPATH, '//a[@href="/account/order-history"]') #История заказов
    logout_btn = (By.XPATH, '//button[contains(text(), "Выход")]') #Кнопка ВЫХОД
    profile_page_description = (By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]') # Текст с описанием в левом углу профиля
    orders_lst = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]') #заказы