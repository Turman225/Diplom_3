import pytest
import allure
import data as data


class TestConstructor:

    @pytest.mark.parametrize('tab, url', [('Конструктор', data.BASE_URL),
                                          ('Лента Заказов', data.FEED_URL)])
    @allure.title("Проверка редиректа при нажатии на кнопку в navbar")
    def test_redirect_pages(self, constructor_page, tab, url):
        constructor_page.open_page(data.LOGIN_URL)
        constructor_page.check_redirect_nav_tab(url, tab)

    @allure.title("Проверка открытия и закрытия модального окна с описанием ингредиентов")
    def test_ingredient_modal_window(self, constructor_page):
        constructor_page.open_page(data.BASE_URL)
        constructor_page.check_modal_window_details_displayed()
        constructor_page.check_modal_window_closed()

    @allure.title("Проверка создания заказа авторизованным пользователем")
    def test_authorization_user_can_create_order(self, constructor_page, login_page):
        constructor_page.open_page(data.BASE_URL)
        login_page.authorization(data.email, data.password)
        constructor_page.click_constructor_btn()
        constructor_page.create_order()

