import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

