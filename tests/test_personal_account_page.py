import allure
import data as data


class TestPersonalAccount:

    def test_redirect_on_click_personal_account_btn(self, personal_acc_page, authorization_page):
        personal_acc_page.open_page(data.BASE_URL)
        authorization_page.authorization(data.email, data.password)
        personal_acc_page.click_personal_acc_btn()
        personal_acc_page.check_redirect_page(data.PROFILE_URL, personal_acc_page.profile_page_description)

    def test_open_orders_history(self, personal_acc_page, authorization_page):
        personal_acc_page.open_page(data.BASE_URL)
        authorization_page.authorization(data.email, data.password)
        personal_acc_page.click_personal_acc_btn()
        personal_acc_page.click_order_history_btn()
        personal_acc_page.check_found_lst_is_not_empty()

    def test_logout(self, personal_acc_page, authorization_page):
        personal_acc_page.open_page(data.BASE_URL)
        authorization_page.authorization(data.email, data.password)
        personal_acc_page.click_personal_acc_btn()
        personal_acc_page.click_logout_btn()
        personal_acc_page.check_logout_successfully()