from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pages.main_page
from base.base_class import Base

class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    l_cart_word = "//div[@class='title']/h1"
    l_cart_name = "//div[@class='cart-item__title']"
    l_cart_price = "//div[@class='cart-item__price__sum']"
    l_cart_sum = "//div[@class='cart-info-pane__sum']"
    l_order = "//button[@class='_button_uzf15_1 _is-medium_uzf15_75 _is-primary_uzf15_270 nowrap cart-info-pane__btn']"

    # Getters
    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_cart_word)))
    def get_cart_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_cart_name)))

    def get_cart_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_cart_price)))

    def get_cart_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_cart_sum)))

    def get_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_order)))

    # Actions
    def click_order(self):
        self.get_order().click()
        print("Click Оформить заказ")

    # Methods
    """проверка цены"""
    def check_price(self):
        cart_price = self.get_cart_price()
        cart_price_value = cart_price.text.replace(" ₽","")
        print("--- Cart_page: price " + cart_price_value)
        self.assert_price(cart_price_value, pages.main_page.main_page_toy_price)

    """проверка Суммы покупки"""
    def check_sum(self):
        cart_sum = self.get_cart_sum()
        cart_sum_value = cart_sum.text.replace(" ₽", "")
        print("--- Cart_page: Sum " + cart_sum_value)
        self.assert_price(cart_sum_value, pages.main_page.main_page_toy_price)

    def check_cart_and_order(self):
        self.assert_word(self.get_cart_word(),"Корзина")            # проверка Корзина
        try:
            if self.get_cart_name():
                print("Товар в корзине")
        except:
            print("Товар отсутствует в корзине")
        self.assert_word(self.get_cart_name(), pages.main_page.main_page_toy_value)  # проверка правильного товара
        print("--- Cart_page: name " + self.get_cart_name().text)
        self.check_price()          # проверка цены
        self.check_sum()             # проверка Суммы покупки
        self.click_order()               # Go to cart
