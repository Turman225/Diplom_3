import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, condition=EC.element_to_be_clickable):
        return WebDriverWait(self.driver, 20).until(condition(locator))

    # Ввод данных в поле
    def write_in_field(self, input=None, text=None):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(input)).send_keys(text)

    @allure.step("Проверка URL")
    def check_url(self, result):
        WebDriverWait(self.driver, 20).until(lambda driver: driver.current_url == result)
        assert self.driver.current_url == result, (f"Проверка URL провалена \n "
                                                   f"Текущий URL = {self.driver.current_url}")

    def check_redirect_page(self, url, locator):
        self.check_url(url)
        assert self.find_element(locator, condition=EC.visibility_of_element_located).is_displayed() == True

    def click_by_script(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
