from selenium.webdriver.common.by import By


class RecoverPasswordLocators:

    recover_pass_btn = (By.LINK_TEXT, 'Восстановить пароль') #Кнопка восстановить пароль
    email_input = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]') #Поле ввода почты
    restore_bnt = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    password_input = (By.XPATH, '//input[@type="password"]') # Поле ввода почты
    code_msg_input = (By.XPATH, '//input[@type="text"]') # Поле ввода кода с письма
    show_pass_btn = (By.XPATH, '//div[@class="input__icon input__icon-action"]') #Кнопка показать пароль
    show_pass_btn_change_type = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]')
    recover_pass_tittle = (By.XPATH, '//h2[contains(text(), "Восстановление пароля")]') # tittle Восстановление пароля
