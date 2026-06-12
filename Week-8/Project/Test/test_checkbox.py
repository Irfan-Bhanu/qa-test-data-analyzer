#from conftest import driver
from pages.checkboxes import checkbox

class TestCheckbox:
    def test_checkbox(self,driver):
            pages= checkbox(driver)

            driver.get("https://the-internet.herokuapp.com/checkboxes")

            if not pages.is_checked():
                pages.select_checkbox1()

            assert pages.is_checked()