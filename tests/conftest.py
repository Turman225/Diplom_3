import pytest
import driver_factory
import data as data
from pages.constructor_page import ConstructorPage
from pages.tape_orders_page import TapeOrdersPage
from pages.recover_password_page import RecoverPasswordPage
from pages.personal_account_page import PersonalAccountPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = driver_factory.WebDriverFactory.create_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def recover_password_page(driver):
    # Создание объекта страницы с драйвером и URL
    page = RecoverPasswordPage(driver, data.LOGIN_URL)
    yield page

@pytest.fixture()
def personal_acc_page(driver):
    # Создание объекта страницы с драйвером и URL
    page = PersonalAccountPage(driver, data.BASE_URL)
    yield page


@pytest.fixture()
def constructor_page(driver):
    # Создание объекта страницы с драйвером и URL
    page = ConstructorPage(driver, data.BASE_URL)
    yield page

@pytest.fixture()
def tape_orders_page(driver):
    # Создание объекта страницы с драйвером и URL
    page = TapeOrdersPage(driver, data.BASE_URL)
    yield page