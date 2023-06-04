
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import baseLogin
from pageobject.locator import elem
from pageobject.data import inputan
import HtmlTestRunner

class TestEditUser(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_edit_user(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baseLogin.test_login(driver)
        driver.find_element(By.XPATH,elem.admin).click() 
        driver.find_element(By.XPATH,elem.edit).click() 
        driver.find_element(By.XPATH,elem.dropdown).click() 
        driver.find_element(By.XPATH,elem.ess).click() 
        # driver.find_element(By.XPATH,xpath.e_name).send_keys(Keys.CONTROL,"a")
        # driver.find_element(By.XPATH,xpath.e_name).send_keys(Keys.DELETE)
        # driver.find_element(By.XPATH,xpath.e_name).send_keys("Odis  Adalwin") 
        driver.find_element(By.XPATH,elem.u_name).send_keys(Keys.CONTROL,"a")
        driver.find_element(By.XPATH,elem.u_name).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH,elem.u_name).send_keys("Ak17") 
        driver.find_element(By.XPATH,elem.save_but).click()
        
        time.sleep(5)
        # driver.find_element(By.CLASS_NAME,xpath.username).clear() 


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportEditUser'))