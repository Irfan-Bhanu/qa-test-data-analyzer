import pytest
import os
import time

from config.config_reader import get_base_url
from pages.login_page import LoginPage
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    #driver.get(get_base_url())  # Juice Shop
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def test_data():
    return {
        "username": "admin",
        "password": "admin",
    }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver=item.funcargs.get("driver")
        if driver:
            time.sleep(1)
            os.makedirs("reports/screenshots", exist_ok=True)

            file_name=item.name.replace("/","_")

            driver.save_screenshot(f"reports/screenshots/{file_name}.png")
