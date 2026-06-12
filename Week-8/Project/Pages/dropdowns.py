from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


from pages.Basepage import Basepage


class DropdownPage(Basepage):

    dropdown = (By.ID, "dropdown")

    def select_by_text(self, text):
        element = self.find(self.dropdown)
        Select(element).select_by_visible_text(text)