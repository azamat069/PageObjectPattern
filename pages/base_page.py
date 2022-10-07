from telnetlib import EC

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = webdriver.Chrome()
        self.url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.browser.implicitly_wait(timeout)
        # self.browser.maximize_window()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
