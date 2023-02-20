from selenium.webdriver.common.by import By


class ElectonicsPage:
    plantonic_xpath = f"// * [text() = 'Plantronics']"
    samsung_xpath = f"// * [text() = 'SAMSUNG']"
    apply_manifacture = "#app > div.page-content > section > div > div > div.row-side > div > dl:nth-child(4) > dd > div > button"
    validate_plantronics = "#app > div.page-content > section > div > div > div.row-body > div:nth-child(1) > div > div > div.row-body > div > div > div:nth-child(2) > div.filter-choices-bar > ul > li:nth-child(1) > span:nth-child(2)"
    validate_samsung = "#app > div.page-content > section > div > div > div.row-body > div:nth-child(1) > div > div > div.row-body > div > div > div:nth-child(2) > div.filter-choices-bar > ul > li:nth-child(1) > span:nth-child(3)"
    select_price = "// * [text() = '$25 - $50']"
    apply_price = "#app > div.page-content > section > div > div > div.row-side > div > dl:nth-child(5) > dd > div.filter-box-bottom > button"
    validate_price = ""

    def __init__(self, driver):
        self.driver = driver

    # TODO select_manifacturer
    def check_manifacture(self):
        self.driver.find_element(By.XPATH, self.plantonic_xpath).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.samsung_xpath).click()
        self.driver.execute_script("window.scrollBy(0, 500)")
        self.driver.find_element(By.CSS_SELECTOR, self.apply_manifacture).click()
        plantonics = self.driver.find_element(By.CSS_SELECTOR, self.validate_plantronics)
        samsung = self.driver.find_element(By.CSS_SELECTOR, self.validate_samsung)
        if plantonics and samsung:
            return True

        # TODO select price
    def check_price(self):
        self.driver.execute_script("window.scrollBy(0,600)")
        self.driver.find_element(By.XPATH, self.select_price).click()
        self.driver.find_element(By.CSS_SELECTOR, self.apply_price).click()

        filter_choices = self.driver.find_elements(By.CLASS_NAME, "filter-choice")
        for elem in filter_choices:
            if elem.text == "$25 - $50":
                return True



    # TODO select customer rating

    # TODO select free shipping

    # TODO enter search within

    # TODO go to next page

    # TODO enable list view

    # TODO click on product

    # TODO add to card




