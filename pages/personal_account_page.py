import data
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage, PersonalAccountLocators):

    def click_personal_acc_btn(self):
        self.click_by_script(PersonalAccountLocators.personal_account)

    def click_order_history_btn(self):
        self.find_element(PersonalAccountLocators.order_history).click()

    def click_logo(self):
        self.click_by_script(PersonalAccountLocators.stellar_logo)

    def click_logout_btn(self):
        self.click_by_script(PersonalAccountLocators.logout_btn)

    def get_order_list(self):
        lst = self.find_elements(PersonalAccountLocators.orders_lst)
        return len(lst)

    def check_found_lst_is_not_empty(self):
        assert self.get_order_list() != 0

    def check_logout_successfully(self):
        self.click_logo()
        self.check_redirect_page(data.BASE_URL, self.stellar_logo)