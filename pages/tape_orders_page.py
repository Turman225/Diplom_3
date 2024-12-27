from locators.tape_orders_locators import TapeOrdersLocators
from pages.constructor_page import ConstructorPage
from pages.personal_account_page import PersonalAccountPage
import allure


class TapeOrdersPage(ConstructorPage, TapeOrdersLocators, PersonalAccountPage):

    id = ''
    initial_count_all_times = ''
    initial_count_today = ''

    def open_first_order(self):
        self.find_element(TapeOrdersLocators.first_order_id).click()

    def get_order_id(self):
        self.wait_change_value_in_element_page(ConstructorPage.order_id, '9999')
        self.id = self.get_text(ConstructorPage.order_id)
        return self.id

    def get_order_in_work(self):
        self.wait_change_value_in_element_page(TapeOrdersLocators.order_in_works, 'Все текущие заказы готовы!')
        order_id = self.get_text(TapeOrdersLocators.order_in_works)
        return order_id

    def get_current_count_today(self):
        self.initial_count_today = self.get_text(TapeOrdersLocators.count_today)
        return self.initial_count_today

    def get_current_count_all_time(self):
        self.initial_count_all_times = self.get_text(TapeOrdersLocators.count_all_times)
        return self.initial_count_all_times

    @allure.step("Проверяем что созданный заказ появился в ленте заказов")
    def check_created_order_has_in_tape(self):
        first_order_id = self.get_text(TapeOrdersLocators.order_id)
        print(first_order_id)
        print(self.id)
        assert f'#0{self.id}' == first_order_id, f'#{self.id} != {first_order_id}'

    @allure.step("Проверяем что созданный заказ появился в истории заказов")
    def check_created_order_has_in_order_history(self):
        self.scroll_to_last_order()
        last_order_id = ''
        list_elem = self.find_elements(PersonalAccountPage.orders_id_in_history)
        if list_elem:
            last_order_id = list_elem[-1].text
            return last_order_id
        else:
           print("Список <li> пуст или не найден.")

        print(last_order_id)
        print(self.id)
        assert f'#0{self.id}' == last_order_id, f'#0{self.id} != {last_order_id}'

    @allure.step("Проверяем что созданный заказ появился в разделе 'В работе'")
    def check_created_order_has_in_work(self):
        assert f'0{self.id}' == self.get_order_in_work(), f'#0{self.id} != {self.get_order_in_work()}'

    @allure.step("Проверяем что модальное окно с описанием заказа открыто")
    def check_modal_window_order_displayed(self):
        assert self.get_text(TapeOrdersLocators.compound_title) == 'Cостав'

    @allure.step("Проверяем что счетчик заказов изменился")
    def check_increment_count(self):
        current_count_all_times = self.get_text(TapeOrdersLocators.count_all_times)
        current_count_today = self.get_text(TapeOrdersLocators.count_today)
        assert (int(self.initial_count_today) < int(current_count_today)) and (int(self.initial_count_all_times) < int(current_count_all_times)),\
        f'{self.initial_count_today} !< {current_count_today}, {self.initial_count_all_times} !< {current_count_all_times})'
