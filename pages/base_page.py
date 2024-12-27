import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Открываем страницу")
    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, condition=EC.element_to_be_clickable, time=10):
        return WebDriverWait(self.driver, time).until(condition(locator))

    def wait_change_value_in_element_page(self, locator, text, time=10,):
        return WebDriverWait(self.driver, time).until_not(EC.text_to_be_present_in_element(locator, text))

    def find_elements(self, locator, condition=EC.visibility_of_any_elements_located, time=10):
        return WebDriverWait(self.driver, time).until(condition(locator))

    def find_element_by_text(self, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(
            (By.XPATH, f'//p[contains(text(), "{text}")]')))

    def get_text(self, locator):
        return self.find_element(locator, condition=EC.visibility_of_element_located).text

    # Ввод данных в поле
    def write_in_field(self, input=None, text=None, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(input)).send_keys(text)

    @allure.step("Проверка URL")
    def check_url(self, expected_url, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.url_to_be(expected_url))
        except TimeoutException:
            raise AssertionError(
                f"Проверка URL провалена\n"
                f"Ожидалось: {expected_url}\n"
                f"Текущий URL: {self.driver.current_url}\n"
                f"Время ожидания: 20 секунд"
            )

    @allure.step("Проверка редиректа на страницу")
    def check_redirect_page(self, url, locator):
        self.check_url(url)
        assert self.find_element(locator, condition=EC.visibility_of_element_located).is_displayed() == True

    @allure.step("Клик на элемент по скрипту")
    def click_by_script(self, locator):
        element = self.find_element(locator)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)