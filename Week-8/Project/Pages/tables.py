from selenium.webdriver.common.by import By

from pages.Basepage import Basepage


class table(Basepage):
    rows=(By.XPATH,"//*[@id='table1']/tbody/tr")

    def get_row_count(self):
        return len(self.driver.find_elements(*self.rows))

    def get_row_data(self,row_number):
        locator=(
            By.XPATH,
            f"//*[@id='table1']/tbody/tr[{row_number}]"
        )
        row = self.driver.find_element(*locator)

        return row.text
