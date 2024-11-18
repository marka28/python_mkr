import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger

main_page_toy_value = 0
main_page_toy_price = 0
main_page_toy_brand = "Большой слон"
main_page_lower_price = 0
main_page_upper_price = 0


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://my-shop.ru/'

    # Locators
    l_catalog = "//span[@class='menu-title']"
    l_toys = "//a[@href='/shop/catalogue/5/sort/a/page/1.html']"
    l_see_all = "//div[@class='more']"
    l_boys = "(//a[@href='/shop/catalogue/3491/sort/a/page/1.html'])[1]"
    l_girls = "(//a[@href='/shop/catalogue/11475/sort/a/page/1.html'])[1]"
    l_main_word_boys_toys = "//*[@id='__nuxt']/div[1]/div/h1/span"
    l_cena_r = "//input[@class='upper-slider']"
    l_filter_cena = "//div[@class='sliders-control']"
    l_all_brands = "//*[@id='__nuxt']/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[3]"
    l_brand = "//div[@title='Большой слон']"
    l_apply_filters = "//button[@class='_button_uzf15_1 _is-medium_uzf15_75 _is-basic_uzf15_190 nowrap _is-expanded_uzf15_210']"
    l_toy_1 = "(//div[@class='item__title__container'])[1]"
    l_toy_1_price = "(//span[@class='price rubl'])[1]"

    # Getters
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_catalog)))

    def get_toys(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_toys)))

    def get_see_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_see_all)))

    def get_boys(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.l_boys)))

    def get_girls(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.l_girls)))

    def get_cena_r(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_cena_r)))

    def get_main_word(self, main_word):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, main_word)))

    def get_all_brands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_all_brands)))

    def get_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_brand)))

    def get_apply_filters(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_apply_filters)))

    def get_toy_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_toy_1)))

    def get_toy_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_toy_1_price)))

    def get_filter_cena(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_filter_cena)))

    # Actions
    def click_catalog(self):
        self.get_catalog().click()
        print("Click 'Каталог'")

    def click_toys(self):
        self.get_toys().click()
        print("Click 'Игрушки''")

    def click_see_all(self):
        self.get_see_all().click()
        print("Click 'Посмотреть всё'")

    def click_boys(self):
        self.get_boys().click()
        print("Click Игрушки для мальчиков")

    def click_girls(self):
        self.get_girls().click()
        print("Click Игрушки для девочек")

    def click_all_brands(self):
        self.get_all_brands().click()
        print("Click Все бренды")

    def click_brand(self):
        self.get_brand().click()
        print("Click Brand")

    def click_apply_filters(self):
        self.get_apply_filters().click()
        print("Click apply_filters")

    def click_toy_1(self):
        self.get_toy_1().click()
        print("Click Toy 1")

    # Methods

    def save_filter_cena(self):
        cena_filter = self.get_filter_cena().get_attribute("style")
        print(cena_filter)

    """Save name to variable"""
    def save_main_toy_name(self):
        self.move_to_element(self.get_toy_1())
        global main_page_toy_value
        main_page_toy_value = self.get_toy_1().text
        print("--- Main_page: Toy name is '" + main_page_toy_value + "'")
        return main_page_toy_value

    """Save price to variable"""
    def save_main_toy_price(self):
        global main_page_toy_price
        main_page_toy_price = self.get_toy_1_price().text
        print("--- Main_page: Toy price is " + main_page_toy_price)
        return main_page_toy_price

    """Select toy by filters"""
    def select_toys(self):
        with allure.step("Select toys"):
            Logger.add_start_step(method="select_toys")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()

            """Select folder in Catalog:"""
            self.click_catalog()     # click : Каталог
            self.click_toys()        # Click : игрушки
            self.click_see_all()     # Click : посмотреть все
            time.sleep(3)
            self.click_girls()      # Click : Игрушки для мальчиков
            time.sleep(3)
                                    # Check that page is correct
            self.assert_word(self.get_main_word(self.l_main_word_boys_toys), "Игрушки для девочек")

            """select the next filters"""
            self.move_to_element(self.get_cena_r())   # перейти к цене
            self.click_cena_r(self.get_cena_r(), 18, 0)      # Сдвинуть ползунок цена
            self.click_all_brands()                 # раскрыть все бренды
            self.click_brand()                      # Выбрать нужный бренд
            self.click_apply_filters()              # применить фильтры

            """Select 1st toy, remember values of name and price """
            self.save_main_toy_name()
            self.save_main_toy_price()
            try:
                self.click_toy_1()
            except:
                print("Нет товаров для выбора, настройте фильтры")
            Logger.add_end_step(url=self.driver.current_url, method="select_toys")
