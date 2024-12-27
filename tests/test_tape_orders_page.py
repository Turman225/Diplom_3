import time

import pytest
import allure
import data as data


class TestTapeOrder:

    @allure.title("Проверка открытия и закрытия модального окна заказа")
    def test_orders_modal_window(self, tape_orders_page, login_page, constructor_page):
        tape_orders_page.open_page(data.BASE_URL)
        login_page.authorization(data.email, data.password)
        constructor_page.click_tape_orders_btn()
        tape_orders_page.open_first_order()
        tape_orders_page.check_modal_window_order_displayed()
        constructor_page.check_modal_window_closed()

    @allure.title("Проверка отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов»")
    def test_user_orders_display_in_order_feed(self, tape_orders_page, login_page, constructor_page, personal_acc_page):
        tape_orders_page.open_page(data.BASE_URL)
        login_page.authorization(data.email, data.password)
        constructor_page.click_constructor_btn()
        constructor_page.create_order()
        tape_orders_page.get_order_id()
        constructor_page.close_modal_window()
        constructor_page.click_tape_orders_btn()
        tape_orders_page.check_created_order_has_in_tape()
        personal_acc_page.click_personal_acc_btn()
        personal_acc_page.click_order_history_btn()
        personal_acc_page.scroll_to_last_order()
        tape_orders_page.check_created_order_has_in_order_history()

    @allure.title("Проверка счетчиков Выполнено при создании заказов")
    def test_created_orders_count(self, tape_orders_page, login_page, constructor_page):
        tape_orders_page.open_page(data.BASE_URL)
        login_page.authorization(data.email, data.password)
        constructor_page.click_tape_orders_btn()
        tape_orders_page.get_current_count_today()
        tape_orders_page.get_current_count_all_time()
        constructor_page.click_constructor_btn()
        constructor_page.create_order()
        constructor_page.click_tape_orders_btn()
        tape_orders_page.check_increment_count()

    def test_created_order_displayed_in_work(self, tape_orders_page, login_page, constructor_page):
        tape_orders_page.open_page(data.BASE_URL)
        login_page.authorization(data.email, data.password)
        constructor_page.click_constructor_btn()
        constructor_page.create_order()
        tape_orders_page.get_order_id()
        constructor_page.close_modal_window()
        constructor_page.click_tape_orders_btn()
        tape_orders_page.get_order_in_work()
        tape_orders_page.check_created_order_has_in_work()