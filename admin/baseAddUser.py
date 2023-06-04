import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pageobject.locator import elem
from pageobject.data import inputan
import baseLogin
import time


def test_add_button(driver):
    driver.find_element(By.XPATH, elem.buttonAdd).click()
    time.sleep(1)