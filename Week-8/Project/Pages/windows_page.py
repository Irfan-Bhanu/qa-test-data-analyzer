from selenium.webdriver.common.by import By

from pages.Basepage import Basepage


class WindowsPage(Basepage):

    click_here= (By.LINK_TEXT,"Click Here")

    def open_new_window(self):
        self.click(self.click_here)
