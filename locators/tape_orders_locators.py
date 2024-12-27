from selenium.webdriver.common.by import By


class TapeOrdersLocators:

    FIRST_ORDER_ID = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li[1]/a')
    COMPOUND_TITLE = (By.XPATH, '//p[@class="text text_type_main-medium mb-8"]')
    ORDER_ID = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    COUNT_ALL_TIMES = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[2]/p[2]']  # счетчик  выполненных заказов за всё время
    COUNT_TODAY = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[3]/p[2]']  # счетчик выполненных заказов за сегодня
    ORDER_IN_WORKS = [By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li']  # заказ в разделе "В работе"