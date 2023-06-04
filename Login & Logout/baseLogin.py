import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PageObject.locator import elem
from PageObject.data import inputan


def test_success_login(driver):
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys(inputan.usernameAdmin)
    time.sleep(3)
    driver.find_element(By.NAME, "password").send_keys(inputan.passwordLogin)
    time.sleep(3)
    driver.find_element(By.XPATH, elem.buttonLoginLoc).click()