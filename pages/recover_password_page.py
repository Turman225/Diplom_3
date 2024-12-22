import data
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.recover_password_locators import RecoverPasswordLocators


class RecoverPasswordPage(BasePage, RecoverPasswordLocators):

    def click_recover_password_btn(self):
        self.find_element(RecoverPasswordLocators.recover_pass_btn).click()

    def fill_email(self):
        self.write_in_field(RecoverPasswordLocators.email_input, data.email)
        self.find_element(RecoverPasswordLocators.restore_bnt).click()

    def fill_password(self):
        self.write_in_field(RecoverPasswordLocators.password_input, data.password)


    def check_password_is_displayed(self):
        self.click_by_script(RecoverPasswordLocators.show_pass_btn)
        attribute = self.find_element(RecoverPasswordLocators.show_pass_btn_change_type, condition=EC.visibility_of_element_located)
        assert attribute is not None
