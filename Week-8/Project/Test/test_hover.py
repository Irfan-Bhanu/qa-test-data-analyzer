from envs.tf_env.Lib.pydoc import visiblename
from selenium.webdriver import ActionChains

from pages.action_page import actionpage

def test_hover(driver):
    driver.get("https://the-internet.herokuapp.com/hovers")

    page = actionpage(driver)

    page.Image1hover()

    assert "name: user1" in page.get_username()

def test_right_click(driver):
    driver.get("https://the-internet.herokuapp.com/context_menu")

    page=actionpage(driver)

    page.right_click()
    
    alert=driver.switch_to.alert

    assert "You selected a context menu"  in alert.text

    alert.accept()
def test_double_click(driver):
    driver.get("https://demoqa.com/buttons")

    page=actionpage(driver)
    page.double_click()
    print(driver.page_source)

    assert ("You have done a double click" in page.get_double_click_message())

def test_drag_and_drop(driver):
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    page=actionpage(driver)
    page.drag_and_drop()

    assert("B" in page.get_column_a_text())
