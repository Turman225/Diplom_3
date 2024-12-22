import allure
import data as data


class TestPersonalAccount:

    def test_redirect_on_click_personal_account_btn(self, personal_acc_page, authorization_page):
        personal_acc_page.open_page(data.BASE_URL)
        personal_acc_page.click_personal_acc_btn()
        authorization_page.authorization(data.email, data.password)
        personal_acc_page.click_personal_acc_btn()
        personal_acc_page.check_redirect_page(data.PROFILE_URL, personal_acc_page.profile_page_description)