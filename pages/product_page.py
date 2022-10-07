import time

from selenium import webdriver
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By

from pages.locators import ProductPageLocators
from base_page import BasePage


class ProductPage():
    def __init__(self, browser, url, timeout=10):
        self.browser = webdriver.Chrome()
        self.url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        self.browser.implicitly_wait(timeout)
        self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)

    def click_add_to_basket(self):
        basket = self.browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
        basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def text_result(self):
        result_text = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/strong').text
        assert 'Coders at Work' == result_text

    def add_product_to_basket(self):
        add_item = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_item.click()



    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message is present"

    def should_dissappear_of_success_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message does not appear"
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message does not disappear"