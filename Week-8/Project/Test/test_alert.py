from pages.alerts import Alertpage


def test_alert(driver):

    page = Alertpage(driver)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    page.click_alert()

    alert = driver.switch_to.alert
    alert.accept()

    assert "You successfully clicked an alert" in page.get_result()

