from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage():
    def __init__(self, browser:RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how,what)
        except NoSuchElementException:
             return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_visibility(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.visibility_of_element_located((how,what)))
        except TimeoutException:
            return False
        return True

    def is_not_visibility(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).\
            until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def try_except(self, item):
        try:
            item.click()
        except:
            self.browser.execute_script('arguments[0].click();', item)