from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


class LoginPage:
    username_id = "labeled-input-signEmail"
    password_id = "labeled-input-password"
    signin_id = "signInSubmit"
    my_profile = '//*[@id="app"]/header/div[1]/div[1]/div[2]/div[4]/a/i[1]'
    logout_path = '//*[@id="app"]/header/div[1]/div[1]/div[2]/div[5]/div/div[1]/div[2]/ul/li[3]/a'
    personal_message = '//*[@id="app"]/div[2]/div[3]/div/div/div[1]/div[1]/div'
    sign_in_page = '//*[@id="app"]/header/div[1]/div[1]/div[2]/div[4]/a/div[2]'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_signin(self):
        self.driver.find_element(By.ID, self.signin_id).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.my_profile)
        self.driver.find_element(By.XPATH, self.logout_path).click()

    def extract_personal_message(self):
        self.driver.implicitly_wait(4)
        return self.driver.find_element(By.XPATH, self.personal_message).text

    def click_login_page(self):
        self.driver.find_element(By.XPATH, self.sign_in_page).click()

