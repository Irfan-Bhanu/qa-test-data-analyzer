from pages.Basepage import Basepage


def test_scroll(driver):

    driver.get(
        "https://the-internet.herokuapp.com/infinite_scroll"
    )

    page = Basepage(driver)

    page.scroll_down()

    page.scroll_down()

    page.scroll_down()

    print(
        page.get_title_js()
    )