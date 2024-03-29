from selenium import webdriver
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import pytest

@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_welcom()
        homepage.click_logout()





