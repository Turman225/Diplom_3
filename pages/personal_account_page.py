import data
import allure
from pages.login_page import LoginPage
from locators.personal_account_locators import PersonalAccountLocators
from pages.recover_password_page import RecoverPasswordPage


class PersonalAccountPage(LoginPage, RecoverPasswordPage):

    def click_personal_acc_btn(self):
        self.click_by_script(PersonalAccountLocators.PERSONAL_ACCOUNT)

    def click_order_history_btn(self):
        self.click_by_script(PersonalAccountLocators.ORDER_HISTORY)

    def click_logo(self):
        self.click_by_script(PersonalAccountLocators.STELLAR_LOGO)

    def click_logout_btn(self):
        self.click_by_script(PersonalAccountLocators.LOGOUT_BTN)

    def get_order_list(self):
        lst = self.find_elements(PersonalAccountLocators.ORDERS_LST)
        return len(lst)

    def scroll_to_last_order(self):
        scrollable_lst = self.find_element(PersonalAccountLocators.ORDER_LIST)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_lst)

    @allure.step("Проверяем что список заказов не пустой")
    def check_found_lst_is_not_empty(self):
        assert self.get_order_list() != 0

    @allure.step("Проверяем выход из аккаунта")
    def check_logout_successfully(self):
        self.check_url(data.LOGIN_URL)
        assert self.find_element(PersonalAccountLocators.LOGIN_ACC).is_displayed() == True