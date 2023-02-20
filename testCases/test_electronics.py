import unittest
from selenium import webdriver

from pageObjects.electonicsPage import ElectonicsPage


class Test_Electronics(unittest.TestCase):
    baseUrl = "https://www.newegg.com/p/pl?N=100164440"

    driver = webdriver.Chrome()
    driver.maximize_window()
    electronicsPage = ElectonicsPage(driver)
    driver.get(baseUrl)

    def test_manifacture_checkbox(self):
        if self.electronicsPage.check_manifacture():
            assert True
        else:
            assert False

    def test_price_checkbox(self):
        if self.electronicsPage.check_price():
            assert True
        else:
            assert False
