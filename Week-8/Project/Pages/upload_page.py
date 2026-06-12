from selenium.webdriver.common.by import By

from pages.Basepage import Basepage


class upload_page(Basepage):

    choose_file= (By.XPATH,"//input[@id='file-upload']")
    upload_file = (By.XPATH,"//input[@id='file-submit']")

    def choose_file_upload(self,filepath):
        self.type(self.choose_file,filepath)

    def upload_file_upload(self):
        self.click(self.upload_file)

