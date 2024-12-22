import data
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage, PersonalAccountLocators):


    def click_personal_acc_btn(self):
        self.find_element(PersonalAccountLocators.personal_account).click()

    def click_order_history_btn(self):
        self.find_element(PersonalAccountLocators.order_history).click()
