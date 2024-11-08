from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import pages.main_page
from base.base_class import Base


class ToyPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    l_toy_name = "//h1[@class='_h1_l3inj_12']"
    l_toy_price = "(//div[@class='price'])[2]"
    l_toy_brand = "//div[@class='font-600 mb-8']"
    l_toy_put_to_cart = "//span[@class='_label_uzf15_28']"
    l_toy_click_cart = "//a[@class='tabs-button orange']"

    # Getters
    def get_toy_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_toy_name)))

    def get_toy_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_toy_price)))

    def get_toy_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_toy_brand)))

    def get_toy_put_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_toy_put_to_cart)))

    def get_toy_click_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_toy_click_cart)))

    # Actions
    def click_put_to_cart(self):
        self.get_toy_put_to_cart().click()
        print("Click В корзину")

    def click_cart(self):
        self.get_toy_click_cart().click()
        print("Click меню Корзина")

    # Methods
    def check_and_put_to_cart(self):
        print("--- Toy_page: name "+self.get_toy_name().text)
        self.assert_word(self.get_toy_name(), pages.main_page.main_page_toy_value)  # проверка правильного товара
        print("--- Toy_page: price " + self.get_toy_price().text)
        self.assert_word(self.get_toy_price(), pages.main_page.main_page_toy_price)  # проверка цены

        print("--- Toy_page: brand " + self.get_toy_brand().text)
        self.assert_word(self.get_toy_brand(), pages.main_page.main_page_toy_brand)  # проверка Бренда

        self.click_put_to_cart()        # Put toy to cart
        self.click_cart()               # Go to cart
        self.assert_url("https://my-shop.ru/my/cart")  # check cart's url
