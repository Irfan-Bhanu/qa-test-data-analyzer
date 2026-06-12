from selenium.webdriver.common.by import By
from pages.Basepage import Basepage
class checkbox(Basepage):

    checkbox1=(By.XPATH,"//*[@id='checkboxes']/input[1]")
    checkbox2=(By.XPATH,"//*[@id='checkboxes']/input[2]")

    def select_checkbox1(self):
        self.click(self.checkbox1)
    def select_checkbox2(self):
        self.click(self.checkbox2)
    def is_checked(self):
        return self.find(self.checkbox1).is_selected()
    def is_unchecked(self):
        return self.find(self.checkbox2).is_selected()


