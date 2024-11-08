import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.toy_page import ToyPage

def test_buy_product_1(set_module):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])  # убирает служебные слова в консоли
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start 'test_buy_product_1'")

    # lp = LoginPage(driver)
    # lp.authorization()                  # Авторизация до выбора товара ( не работает! капча!)

    mp = MainPage(driver)
    mp.select_toys()                    # Выбрать товар и перейти на его страницу

    tp = ToyPage(driver)
    tp.check_and_put_to_cart()          # Страница товара - проверить наименование, цену и положить в корзину, перейти в корзину

    cp = CartPage(driver)
    cp.check_cart_and_order()           # Корзина - проверить товар и цена в корзине. Перейти к оформлению

    lp = LoginPage(driver)
    lp.authorization()                  # Авторизация после выбора товара

    op = OrderPage(driver)
    op.check_order_sum()                 # проверка суммы к Оплате

    time.sleep(3)
    driver.quit()
