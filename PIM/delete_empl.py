import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baselogin
from PageObject.locator import elem
from PageObject.dataInput import input
import HtmlTestRunner

class TestDeleteEmployee(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_Success_Delete_Employee(self): #test cases 1
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_trash).click()
        driver.find_element(By.XPATH, elem.btn_delete).click()
        

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_Delete_Employee'))