from selenium.webdriver.common.by import By


class ConstructorLocators:

    constructor_title = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')
    constructor_btn = (By.XPATH, '//p[contains(text(), "Конструктор")]')
    orders_tape_title = (By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"]')
    orders_tape_btn = (By.XPATH, '//p[contains(text(), "Лента Заказов")]')
    buns = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')
    buns_counter = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]/div[1]/p')
    stuffing_tab = (By.XPATH, '//span[contains(text(), "Начинки"]')
    meat = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]')
    basket = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    description_title = (By.XPATH, '//h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"]')
    close_modal_btn = (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button')
    create_order_btn = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    order_status = (By.XPATH, '//p[@class="undefined text text_type_main-small mb-2"]')