
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pageobject.locator import elem
from pageobject.data import inputan

def test_login(driver): 
    time.sleep(1)
    driver.find_element(By.NAME, "username").send_keys(inputan.usernameAdmin)
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(inputan.passwordLogin)
    time.sleep(1)
    driver.find_element(By.XPATH, elem.buttonLoginLoc).click()
