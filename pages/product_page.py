from selenium import webdriver
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By


class ProductPage():
    def __init__(self, browser, url, timeout=10):
        self.browser = webdriver.Chrome()
        self.url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
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


