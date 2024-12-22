from selenium import webdriver

class WebDriverFactory:
    @staticmethod
    def create_driver(browser_name):
        if browser_name == "chrome":
            return webdriver.Chrome()
        elif browser_name == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Браузер не подключен : {browser_name}")
