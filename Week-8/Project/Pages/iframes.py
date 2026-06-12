from selenium.webdriver.common.by import By


from pages.Basepage import Basepage


class FramePage(Basepage):

    iframe = (By.ID, "mce_0_ifr")
    text_box = (By.ID, "tinymce")

    def switch_to_frame(self):
        self.driver.switch_to.frame(self.find(self.iframe))

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def type_text(self, text):
        self.type(self.text_box, text)