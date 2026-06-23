from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.Basepage import Basepage


class actionpage(Basepage):
    Image1=(By.XPATH,'//*[@id="content"]/div/div[1]/img')
    User1 = (By.XPATH, "//h5[text()='name: user1']")
    right_click_box =(By.ID,"hot-spot")
    double_click_btn= (By.ID,"doubleClickBtn")
    double_click_message=(By.ID,"doubleClickMessage")
    source=(By.ID,"column-a")
    target=(By.ID,"column-b")

    def Image1hover(self):
        image = self.find(self.Image1)
        ActionChains(self.driver).move_to_element(image).perform()

    def get_username(self):
        return self.get_text(self.User1)

    def right_click(self):
        element= self.find(self.right_click_box)
        ActionChains(self.driver).context_click(element).perform()

    def double_click(self):
        element1=self.find(self.double_click_btn)
        print("Button text:", element1.text)
        ActionChains(self.driver).double_click(element1).perform()

    def get_double_click_message(self):
        return self.get_text(self.double_click_message)

    def drag_and_drop(self):
        element3=self.find(self.source)
        element4=self.find(self.target)
        ActionChains(self.driver).drag_and_drop(element3,element4).perform()

    def get_column_a_text(self):
         return self.find(self.source).text

