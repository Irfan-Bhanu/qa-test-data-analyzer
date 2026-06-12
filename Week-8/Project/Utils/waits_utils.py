from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class wait_utils():

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def wait_for_element(self,locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def wait_for_clickable(self,locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_visibility(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_invisible(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element(locator))






