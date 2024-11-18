import datetime
import os
from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url =self.driver.current_url
        print("Current url: " + get_url)

    """Methor assert words"""
    def assert_word(self, word, result):
        value_word = word.text
      #  print(value_word)
        assert value_word == result , print(value_word)
        print("Word '"+result+"' is correct")

    """Methor assert price """
    def assert_price(self, price, result):
       #  print(price)
        assert price == result , print(price)
        print("Price(Sum) '"+result+"' is correct")


    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'

        # self.driver.save_screenshot('C:\\Users\\marina\\PycharmProjects\\main_mkr\\screen\\' + name_screenshot)
        p_screen = os.getcwd()
        if p_screen[p_screen.rfind('\\')+ 1:].split()[0] == 'main_mkr':
            self.driver.save_screenshot(f"screen/{name_screenshot}")
        elif p_screen[p_screen.rfind('\\')+ 1:].split()[0] == 'tests':
            self.driver.save_screenshot(f"../screen/{name_screenshot}")

        print("Screenshot for finish page is created in SCREEN folder")

    """Methor assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        print(get_url)
        assert get_url == result
        print("Url is correct")

    """Method move focus to element"""
    def move_to_element(self,element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    """Method move focus to element"""
    def click_cena_r(self, element, x, y ):
        action = ActionChains(self.driver)
        action.click_and_hold(element).move_by_offset(x,y).release().perform()      # ПОЛЗУНОК цена правый
        print("Element is scrolled")