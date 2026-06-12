from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config_reader import get_browser
from config.config_reader import get_base_url

def get_driver():

    browser = get_browser()

    if browser == 'chrome':
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        raise Exception('browser must be chrome')

    driver.maximize_window()
    return driver