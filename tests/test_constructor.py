import pytest
import allure
import data as data


class TestConstructor:

    @pytest.mark.parametrize('tab, url', [('Конструктор', data.BASE_URL),
                                          ('Лента Заказов', data.FEED_URL)])
    def test_redirect_pages(self, constructor_page, tab, url):
        constructor_page.open_page(data.LOGIN_URL)
        constructor_page.check_redirect_nav_tab(url, tab)

    def test_modal_window(self, constructor_page):
        constructor_page.open_page(data.BASE_URL)
        constructor_page.check_modal_window_displayed()
        constructor_page.check_modal_window_closed()

    def test_create_order(self, constructor_page, authorization_page):
        constructor_page.open_page(data.BASE_URL)
        authorization_page.authorization(data.email, data.password)
        constructor_page.click_constructor_btn()
        constructor_page.add_buns()
        # constructor_page.click_create_order_btn()
