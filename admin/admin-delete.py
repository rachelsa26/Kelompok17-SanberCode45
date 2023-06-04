import unittest
import time
import baselogin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from random import randint
from pageobject.locator import elem
from pageobject.data import inputan
import HtmlTestRunner

class TestEditUser(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_delete_user(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elem.admin).click() 
        driver.find_element(By.XPATH,elem.deleted).click() 
        driver.find_element(By.XPATH,elem.cfrm_deleted).click() 
        
        time.sleep(5)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportDeleteUser'))