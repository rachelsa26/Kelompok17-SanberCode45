import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baselogin
from PageObject.locator import elem
from PageObject.dataInput import input


def test_a_Success_add_employee(driver): #test cases 1

    driver.get(input.baseUrl)
    baselogin.test_login(driver)
    driver.find_element(By.XPATH, elem.btn_PIM).click()
    driver.find_element(By.XPATH, elem.btn_add_empl).click()
    driver.find_element(By.NAME, elem.firsname).send_keys(input.firstname)
    driver.find_element(By.NAME, elem.lastname).send_keys(input.lastname)
    driver.find_element(By.XPATH, elem.hps_id).clear()
    driver.find_element(By.XPATH, elem.id_empl).send_keys(input.id_empl)
    driver.find_element(By.XPATH, elem.btn_save_add).click()