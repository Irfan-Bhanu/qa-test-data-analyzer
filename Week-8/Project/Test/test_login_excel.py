import pytest

from pages.login_page import LoginPage
from utils.data_reader import read_excel_data

data= read_excel_data("login_data.xlsx")

@pytest.mark.parametrize(
    "username,password,expected",
    data
)

def test_login(driver,username, password,expected):
    driver.get("https://the-internet.herokuapp.com/login")

    page = LoginPage(driver)

    page.enter_username(username)

    page.enter_password(password)

    page.click_login()

    current_url = driver.current_url

    if expected == "success":

        assert "secure" in current_url

    else:

        assert "login" in current_url