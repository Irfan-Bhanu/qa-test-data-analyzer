from pages.dropdowns import DropdownPage


def test_dropdown(driver):

    page = DropdownPage(driver)

    driver.get("https://the-internet.herokuapp.com/dropdown")

    page.select_by_text("Option 1")

    assert "Option 1" in driver.page_source