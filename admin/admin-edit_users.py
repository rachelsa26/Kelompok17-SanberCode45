
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import baselogin
from pageobject.locator import xpath


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_edit_user(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,xpath.admin).click() 
        driver.find_element(By.XPATH,xpath.edit).click() 
        driver.find_element(By.XPATH,xpath.dropdown).click() 
        driver.find_element(By.XPATH,xpath.ess).click() 
        # driver.find_element(By.XPATH,xpath.e_name).send_keys(Keys.CONTROL,"a")
        # driver.find_element(By.XPATH,xpath.e_name).send_keys(Keys.DELETE)
        # driver.find_element(By.XPATH,xpath.e_name).send_keys("Odis  Adalwin") 
        driver.find_element(By.XPATH,xpath.u_name).send_keys(Keys.CONTROL,"a")
        driver.find_element(By.XPATH,xpath.u_name).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH,xpath.u_name).send_keys("Ak17") 
        driver.find_element(By.XPATH,xpath.save_but).click()
        
        time.sleep(5)
        # driver.find_element(By.CLASS_NAME,xpath.username).clear() 
        




    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()