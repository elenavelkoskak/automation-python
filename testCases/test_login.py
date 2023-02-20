import pytest
from selenium import webdriver

from pageObjects.loginPage import LoginPage

class Test_Login:
    baseUrl = "https://www.newegg.com/"
    username = "test_tester@hotmail.com"
    password = "Testerpassword123"


    def test_homepage_title(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.loginpage = LoginPage(self.driver)

        self.driver.get(self.baseUrl)
        self.loginpage.click_login_page()

        self.loginpage.setUserName(self.username)
        self.loginpage.click_signin()
        self.loginpage.setPassword(self.password)
        self.loginpage.click_signin()

        personal_message = self.loginpage.extract_personal_message()
        self.driver.close()
        if personal_message == "HI, TEST TESTER":
            assert True
        else:
            assert False


