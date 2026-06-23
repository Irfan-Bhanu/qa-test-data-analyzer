from pages.windows_page import WindowsPage


def test_windows(driver):

    driver.get("https://the-internet.herokuapp.com/windows")

    page=WindowsPage(driver)

    parent=driver.current_window_handle
    page.open_new_window()

    all_windows= driver.window_handles
    for window in all_windows:
        if window!=parent:
            driver.switch_to.window(window)

    assert "New Window" in driver.page_source

    driver.close()

    driver.switch_to.window(parent)

    assert "Opening a new window" in driver.page_source
