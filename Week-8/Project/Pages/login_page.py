

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from config.config_reader import get_base_url
from pages.Basepage import Basepage


class LoginPage(Basepage):

    basicauth= (By.XPATH, '//*[@id="content"]/ul/li[3]/a')
#//a[text()='Basic Auth']
        # Locators
    def open_home(self):
        self.driver.get(get_base_url())

    def click_basic_auth(self):
        self.click(self.basicauth)


    def open_basic_auth_direct(self, username, password):
        url = f"http://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(url)

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.XPATH, "//button")

    def enter_username(self, username):
        self.type(self.username, username)

    def enter_password(self, password):
        self.type(self.password, password)

    def click_login(self):
        self.click(self.login_button)




