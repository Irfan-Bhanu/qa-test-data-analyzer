from selenium.common import StaleElementReferenceException

from utils.waits_utils import  wait_utils

class Basepage:

    def __init__(self, driver):
        self.driver = driver
        self.wait= wait_utils(driver)

    def find(self,locator):
        return self.wait.wait_for_element(locator)

    def click(self,locator):
        self.wait.wait_for_clickable(locator).click()

    def type(self,locator,text):
        self.find(locator).send_keys(text)

    def get_text(self,locator):
        return self.find(locator).text

    def safe_click(self, locator):
        element = self.wait.wait_for_clickable(locator)
        element.click()

    from selenium.common.exceptions import StaleElementReferenceException

    def safe_click1(self, locator):
        for _ in range(3):
            try:
                element = self.wait.wait_for_clickable(locator)
                element.click()
                return
            except StaleElementReferenceException:
                print("Retrying click due to stale element...")

    def click_dynamic_button(self):
        self.safe_click(self.dynamic_button)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        return self.driver.switch_to.alert.text