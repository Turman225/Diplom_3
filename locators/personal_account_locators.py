from selenium.webdriver.common.by import By


class PersonalAccountLocators:

    personal_account = (By.LINK_TEXT, '/account')  # Кнопка "Личный кабинет"
    order_history = (By.LINK_TEXT, '/account/order-history') #История заказов
    logout_btn = (By.XPATH, '//button[@class=Account_button__14Yp3 text text_type_main-medium text_color_inactive"]') #Кнопка ВЫХОД
    profile_page_description = (By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]') # Текст с описанием в левом углу профиля