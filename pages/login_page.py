import data
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    login_in_account = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    email_input = (By.XPATH, '//input[@type="text"]')
    password_input = (By.XPATH, '//input[@type="password"]')
    login_btn = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')

    def authorization(self, mail, password):
        self.find_element(self.login_in_account).click()
        self.write_in_field(self.email_input, mail)
        self.write_in_field(self.password_input, password)
        self.find_element(self.login_btn).click()