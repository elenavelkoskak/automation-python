from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://selenium-python.readthedocs.io/locating-elements.html")

a = driver.find_element(By.ID, "locating-by-id")

print(a.text)
