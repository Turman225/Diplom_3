from selenium.webdriver.common.by import By


class TapeOrdersLocators:

    first_order_id = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li[1]/a')
    compound_title = (By.XPATH, '//p[@class="text text_type_main-medium mb-8"]')
    order_id = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    count_all_times = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[2]/p[2]']  # счетчик  выполненных заказов за всё время
    count_today = [By.XPATH, '//div[@class="OrderFeed_ordersData__1L6Iv"]/div[3]/p[2]']  # счетчик выполненных заказов за сегодня
    order_in_works = [By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li']  # заказ в разделе "В работе"