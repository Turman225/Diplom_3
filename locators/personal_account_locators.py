from selenium.webdriver.common.by import By


class PersonalAccountLocators:

    stellar_logo = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a')
    personal_account = (By.XPATH, '//a[@href="/account"]')  # Кнопка "Личный кабинет"
    login_acc = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    order_history = (By.XPATH, '//a[@href="/account/order-history"]') #История заказов
    order_list = (By.XPATH, '//ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]')
    orders_id_in_history = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]/a/div[1]/p[1]')

    logout_btn = (By.XPATH, '//button[contains(text(), "Выход")]') #Кнопка ВЫХОД
    profile_page_description = (By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]') # Текст с описанием в левом углу профиля
    orders_lst = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"]') #заказы