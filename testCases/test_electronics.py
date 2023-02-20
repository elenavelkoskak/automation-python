import pytest
from selenium import webdriver

from pageObjects.electonicsPage import ElectonicsPage

class Test_Electronics:
    baseUrl = "https://www.newegg.com/p/pl?N=100164440"

    def test_electronics_page(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.electronicsPage = ElectonicsPage(self.driver)

        self.driver.get(self.baseUrl)

        if self.electronicsPage.check_manifacture():
            assert True

