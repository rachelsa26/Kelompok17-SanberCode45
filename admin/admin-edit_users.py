
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

    def test_edit_user(self): #test success edit users at admin
        username = "".join([chr(randint(65, 90)) for _ in range(randint(6, 12))])
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elem.admin).click() 
        driver.find_element(By.XPATH,elem.edit).click() 
        driver.find_element(By.XPATH,elem.dropdown).click()
        driver.find_element(By.XPATH,elem.admin_user).click()
        driver.find_element(By.XPATH, elem.statusAddUserLoc).click()
        driver.find_element(By.XPATH, elem.statusEnabledAddUserLoc).click()
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys(Keys.CONTROL,"a")
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys("a")
        driver.find_element(By.XPATH, elem.e_name).click() 
        driver.find_element(By.XPATH,elem.u_name).send_keys(Keys.CONTROL,"a")
        driver.find_element(By.XPATH,elem.u_name).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH,elem.u_name).send_keys(username) 
        driver.find_element(By.XPATH,elem.check_pass).click()
        driver.find_element(By.XPATH,elem.passwrd).send_keys("123456789a") 
        driver.find_element(By.XPATH,elem.cfrm_passwrd).send_keys("123456789a") 
        driver.find_element(By.XPATH,elem.save_but).click()
        
        time.sleep(5)
        
    def test_failed_edit_userrole(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elem.admin).click() 
        driver.find_element(By.XPATH,elem.edit).click() 
        driver.find_element(By.XPATH,elem.dropdown).click()
        driver.find_element(By.XPATH,elem.select).click()
        

        validation = driver.find_element(By.XPATH, elem.textRequiredUserRoleAddUserLoc).text
        self.assertEqual(validation, "Required")
        
        time.sleep(5)

    def test_failed_edit_user_status(self): #test success edit users at admin
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elem.admin).click() 
        driver.find_element(By.XPATH,elem.edit).click() 
        driver.find_element(By.XPATH,elem.dropdown).click()
        driver.find_element(By.XPATH,elem.admin_user).click()
        driver.find_element(By.XPATH, elem.statusAddUserLoc).click()
        driver.find_element(By.XPATH, elem.select_status).click()


        validation = driver.find_element(By.XPATH, elem.textRequiredStatusAddEmployeeLoc).text
        self.assertEqual(validation, "Required")
        
        time.sleep(5)

    def test_failed_edit_user_name(self): #test success edit users at admin
        
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elem.admin).click() 
        driver.find_element(By.XPATH,elem.edit).click() 
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys(Keys.CONTROL,"a")
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH,elem.save_but).click()
        time.sleep(10)
        


        validation = driver.find_element(By.XPATH, elem.textRequiredEmployeeNameAddUserLoc).text
        self.assertEqual(validation, "Required")
        
        time.sleep(5)

    def test_failed_edit_user_username(self): #test success edit users at admin
        
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elem.admin).click() 
        driver.find_element(By.XPATH,elem.edit).click() 
        driver.find_element(By.XPATH, elem.u_name).send_keys(Keys.CONTROL,"a")
        driver.find_element(By.XPATH, elem.u_name).send_keys(Keys.DELETE)
        time.sleep(2)
        driver.find_element(By.XPATH,elem.save_but).click()
        time.sleep(10)
        


        validation = driver.find_element(By.XPATH, elem.textRequiredUsernameAddUserLoc).text
        self.assertEqual(validation, "Required")
        
        time.sleep(5)
        
    def test_failed_edit_user_password(self): #test success edit users at admin
        
        driver = self.browser
        driver.implicitly_wait(20)
        driver.get(inputan.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH,elem.admin).click() 
        driver.find_element(By.XPATH,elem.edit).click() 
        driver.find_element(By.XPATH,elem.check_pass).click()
        time.sleep(2)
        driver.find_element(By.XPATH,elem.save_but).click()
        time.sleep(10)
        


        validation = driver.find_element(By.XPATH, elem.textRequiredPasswordAddUserLoc).text
        self.assertEqual(validation, "Required")
        
        time.sleep(5)
        


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportEditUser'))