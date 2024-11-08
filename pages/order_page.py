from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pages.main_page
from base.base_class import Base

class OrderPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    l_order_word = "//header[@class='header']/h1"
    l_order_sum = "//*[@id='order_confirmation']/div/div[3]/div[2]"

    # Getters
    def get_order_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_order_word)))
    def get_order_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_order_sum)))

    # Actions

    # Methods
    def check_order_sum(self):
        self.assert_word(self.get_order_word(), "Оформление заказа")  # проверка страницы Оформление заказа
        order_sum = self.get_order_sum()
        order_sum_value = order_sum.text
        print("--- Order_page: Sum_k_oplate  " + order_sum_value)
        self.assert_price(order_sum_value, pages.main_page.main_page_toy_price)     # проверка суммы заказа
        print("Перешли к оплате товара")