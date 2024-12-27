import allure
import data as data


class TestRecoverPasswordPage:

    @allure.title("Проверка редиректа при нажатии на кнопку 'Восстановить пароль'")
    def test_redirect_page_at_click_btn(self, recover_password_page):
        recover_password_page.open_page(data.LOGIN_URL)
        recover_password_page.click_recover_password_btn()
        recover_password_page.check_redirect_page(data.FORGOT_PASS_URL, recover_password_page.recover_pass_tittle)

    @allure.title("Проверка редиректа при заполнении почты и нажатии на кнопку ВОССТАНОВИТЬ")
    def test_fill_email_and_click_btn(self, recover_password_page):
        recover_password_page.open_page(data.FORGOT_PASS_URL)
        recover_password_page.fill_email()
        recover_password_page.check_redirect_page(data.RESET_PASS_URL, recover_password_page.password_input)

    @allure.title("Проверка работы кнопки показа пароля")
    def test_show_password_btn(self, recover_password_page):
        recover_password_page.open_page(data.FORGOT_PASS_URL)
        recover_password_page.fill_email()
        recover_password_page.fill_password()
        recover_password_page.check_password_is_displayed()