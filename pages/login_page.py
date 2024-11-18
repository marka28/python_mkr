import time
import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):

    url = 'https://my-shop.ru/'


    # Locators
    l_login_user_button = "//a[@class='tabs-button']"
    l_pas_button = "//*[@id='__nuxt']/div[2]/div/div[3]/div[5]/button"
    l_mail = "//input[@id='email']"
    l_password = "//input[@id='pass']"
    l_show_pass = "//span[@class='_show-label_1a5e1_90']"
    l_login_button = "//button[@class='_button_uzf15_1 _is-large_uzf15_100 _is-basic_uzf15_190 nowrap _is-expanded_uzf15_210']"
    l_main_word = "//span[@class='title']"

    # Getters
    def get_login_user_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_login_user_button)))

    def get_pass_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_pas_button)))
    def get_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_mail)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_password)))

    def get_show_pass(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_show_pass)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.l_main_word)))

    # Actions
    def input_mail(self, user_name):
        self.get_mail().send_keys(user_name)
        print("Input e-mail")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_pass_button(self):
        self.get_pass_button().click()
        print("Click Войти по паролю")

    def click_show_pass(self):
        self.get_show_pass().click()
        print("Click Показать пароль")

    def click_login_button(self):
        try:
            self.get_login_button().click()
            print("Click Войти")
        except:
            print("---!!!Click Войти FAILURE !!!---")

    def click_login_user_button(self):
        self.get_login_user_button().click()
        print("Click войти в кабинет")

    # Methods
    """Authorization"""
    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            time.sleep(3)
            try:
                self.click_login_user_button()      # Вход в ЛК
                time.sleep(3)
            except:
                print("пропуск шага")
            self.click_pass_button()            # Вход через почту
            self.input_mail("semnastya23@gmail.com")
            time.sleep(2)
            self.input_password("St_msh_11")
            time.sleep(3)
            # self.click_show_pass()
            self.click_login_button()
            time.sleep(2)
            self.assert_url("https://my-shop.ru/my/orders/new")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")