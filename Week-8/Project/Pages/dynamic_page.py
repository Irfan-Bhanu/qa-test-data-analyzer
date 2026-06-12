from selenium.webdriver.common.by import By
from pages.Basepage import Basepage

class DynamicPage(Basepage):

    remove_button = (By.XPATH, "//button[text()='Remove']")
    message = (By.ID, "message")

    def click_remove(self):
        self.safe_click(self.remove_button)

    def get_message(self):
        return self.get_text(self.message)


