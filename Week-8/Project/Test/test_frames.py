from pages.iframes import FramePage


def test_frame(driver):

    page = FramePage(driver)

    driver.get("https://the-internet.herokuapp.com/iframe")

    page.switch_to_frame()

    page.type_text("Hello Frame")

    assert "Hello Frame" in driver.page_source

    page.switch_to_default()