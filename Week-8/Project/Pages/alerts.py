from selenium.webdriver.common.by import By

from pages.Basepage import Basepage


class Alertpage(Basepage):

    js_alert = (By.XPATH,"//button[text()='Click for JS Alert']")
    result = (By.ID,"result")

    def click_alert(self):
        self.click(self.js_alert)
    def get_result(self):
        return self.get_text(self.result)

