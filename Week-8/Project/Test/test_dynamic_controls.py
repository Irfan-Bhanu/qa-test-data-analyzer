from pages import Basepage, dynamic_page
from pages.dynamic_page import DynamicPage


def test_dynamic_controls(login_page, driver):
    dynamic_page = DynamicPage(driver)
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")


    #Basepage.click_dynamic_button()
    dynamic_page.click_remove()

    assert "It's gone!" in driver.page_source