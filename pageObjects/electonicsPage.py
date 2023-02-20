from selenium.webdriver.common.by import By


class ElectonicsPage:
    click_plantronics = "#app > div.page-content > section > div > div > div.row-side > div > dl:nth-child(4) > dd > ul:nth-child(1) > li:nth-child(1) > div > label > span"
    click_samsung = "#app > div.page-content > section > div > div > div.row-side > div > dl:nth-child(4) > dd > ul:nth-child(1) > li:nth-child(3) > div"
    apply = "#app > div.page-content > section > div > div > div.row-side > div > dl:nth-child(4) > dd > div > button"
    validate_plantronics = "#app > div.page-content > section > div > div > div.row-body > div:nth-child(1) > div > div > div.row-body > div > div > div:nth-child(2) > div.filter-choices-bar > ul > li:nth-child(1) > span:nth-child(2)"
    validate_samsung = "#app > div.page-content > section > div > div > div.row-body > div:nth-child(1) > div > div > div.row-body > div > div > div:nth-child(2) > div.filter-choices-bar > ul > li:nth-child(1) > span:nth-child(3)"


    def __init__(self, driver):
        self.driver = driver

    # TODO select_manifacturer
    def check_manifacture(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_plantronics).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, self.click_samsung).click()
        self.driver.execute_script("window.scrollBy(0, 500)")
        self.driver.find_element(By.CSS_SELECTOR, self.apply).click()
        plantonics = self.driver.find_element(By.CSS_SELECTOR, self.validate_plantronics)
        samsung = self.driver.find_element(By.CSS_SELECTOR, self.validate_samsung)
        if plantonics and samsung:
            return True

    # TODO select price

    # TODO select customer rating

    # TODO select free shipping

    # TODO enter search within

    # TODO go to next page

    # TODO enable list view

    # TODO click on product

    # TODO add to card




