import data
import allure
from pages.login_page import LoginPage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(LoginPage, PersonalAccountLocators):

    def click_personal_acc_btn(self):
        self.click_by_script(PersonalAccountLocators.personal_account)

    def click_order_history_btn(self):
        self.click_by_script(PersonalAccountLocators.order_history)

    def click_logo(self):
        self.click_by_script(PersonalAccountLocators.stellar_logo)

    def click_logout_btn(self):
        self.click_by_script(PersonalAccountLocators.logout_btn)

    def get_order_list(self):
        lst = self.find_elements(PersonalAccountLocators.orders_lst)
        return len(lst)

    def scroll_to_last_order(self):
        scrollable_lst = self.find_element(PersonalAccountLocators.order_list)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_lst)

    @allure.step("Проверяем что список заказов не пустой")
    def check_found_lst_is_not_empty(self):
        assert self.get_order_list() != 0

    @allure.step("Проверяем выход из аккаунта")
    def check_logout_successfully(self):
        self.check_url(data.LOGIN_URL)
        assert self.find_element(PersonalAccountLocators.login_acc).is_displayed() == True