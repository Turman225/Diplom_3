import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage, ConstructorLocators):

    def click_constructor_btn(self):
        self.click_by_script(ConstructorLocators.constructor_btn)

    def click_to_bun(self):
        self.find_element(ConstructorLocators.buns).click()

    def click_create_order_btn(self):
        self.find_element(ConstructorLocators.create_order_btn).click()
        time.sleep(5)
        assert self.get_text(ConstructorLocators.order_status) == 'Ваш заказ начали готовить'

    def close_modal_window(self):
        self.find_element(ConstructorLocators.close_modal_btn).click()

    def add_buns(self):
        actions = ActionChains(self.driver)
        ingredient = self.find_element(ConstructorLocators.buns)
        basket_lst = self.find_element(ConstructorLocators.basket)
        actions.click_and_hold(ingredient).move_to_element(basket_lst).release().perform()
        assert self.get_text(ConstructorLocators.buns_counter) == '2', f'Фактический результат {self.get_text(ConstructorLocators.buns_counter)}'
        time.sleep(5)

    def check_modal_window_displayed(self):
        self.click_to_bun()
        assert self.get_text(ConstructorLocators.description_title) == 'Детали ингредиента'

    def check_modal_window_closed(self):
        self.close_modal_window()
        assert self.find_element(ConstructorLocators.description_title, condition=EC.invisibility_of_element)

    def check_redirect_nav_tab(self, url, elem):
        if elem == 'Конструктор':
            self.click_constructor_btn()
            self.check_redirect_page(url, ConstructorPage.constructor_title)
        if elem == 'Лента заказов':
            self.check_redirect_page(url, ConstructorPage.orders_tape_title)
            self.click_by_script(ConstructorLocators.orders_tape_btn)

