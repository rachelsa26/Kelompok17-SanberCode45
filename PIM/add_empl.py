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


class TestAddEmployee(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_Success_add_employee(self): #test cases 1
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_add_empl).click()
        driver.find_element(By.NAME, elem.firsname).send_keys(input.firstname)
        driver.find_element(By.NAME, elem.lastname).send_keys(input.lastname)
        driver.find_element(By.XPATH, elem.hps_id).clear()
        driver.find_element(By.XPATH, elem.id_empl).send_keys(input.id_empl)
        driver.find_element(By.XPATH, elem.btn_save_add).click()
        
    def test_a_add_employee_with_createLogin(self): #test cases 2
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_add_empl).click()
        driver.find_element(By.NAME, elem.firsname).send_keys(input.firstname)
        driver.find_element(By.NAME, elem.middle_name).send_keys(input.middlename)
        driver.find_element(By.NAME, elem.lastname).send_keys(input.lastname)
        driver.find_element(By.XPATH, elem.hps_id).clear()
        driver.find_element(By.XPATH, elem.id_empl).send_keys(input.id_empl)
        driver.find_element(By.XPATH, elem.btn_crt_lgn).click()
        driver.find_element(By.XPATH, elem.username).send_keys(input.username)
        driver.find_element(By.XPATH, elem.password).send_keys(input.password)
        driver.find_element(By.XPATH, elem.confirm_psw).send_keys(input.confir_pasw)
        driver.find_element(By.XPATH, elem.btn_save_add).click()

    def test_a_empty_employee_id(self): #test cases 3
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_add_empl).click()
        driver.find_element(By.NAME, elem.firsname).send_keys(input.firstname)
        driver.find_element(By.NAME, elem.middle_name).send_keys(input.middlename)
        driver.find_element(By.NAME, elem.lastname).send_keys(input.lastname)
        driver.find_element(By.XPATH, elem.btn_save_add).click()

    def test_a_Failed_empty_lastname(self): #test cases 4
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_add_empl).click()
        driver.find_element(By.NAME, elem.firsname).send_keys(input.firstname)
        driver.find_element(By.NAME, elem.middle_name).send_keys(input.middlename)
        driver.find_element(By.XPATH, elem.hps_id).clear()
        driver.find_element(By.XPATH, elem.id_empl).send_keys(input.id_empl)
        driver.find_element(By.XPATH, elem.btn_save_add).click()
        validation = driver.find_element(By.XPATH, elem.status_empty).text
        self.assertEqual(validation, "Required")

    def test_a_empty_employee_FirstName(self): #test cases 5
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_add_empl).click()
        driver.find_element(By.NAME, elem.middle_name).send_keys(input.middlename)
        driver.find_element(By.NAME, elem.lastname).send_keys(input.lastname)
        driver.find_element(By.XPATH, elem.hps_id).clear()
        driver.find_element(By.XPATH, elem.id_empl).send_keys(input.id_empl)
        driver.find_element(By.XPATH, elem.btn_save_add).click()

    def test_a_Failed_empty_Fullname(self): #test cases 6
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_add_empl).click()
        driver.find_element(By.XPATH, elem.hps_id).clear()
        driver.find_element(By.XPATH, elem.id_empl).send_keys(input.id_empl)
        driver.find_element(By.XPATH, elem.btn_save_add).click()
        validation = driver.find_element(By.XPATH, elem.status_empty).text
        self.assertEqual(validation, "Required")
    
    def test_a_add_employee_with_Empty_Password(self): #test cases 7
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_add_empl).click()
        driver.find_element(By.NAME, elem.firsname).send_keys(input.firstname)
        driver.find_element(By.NAME, elem.middle_name).send_keys(input.middlename)
        driver.find_element(By.NAME, elem.lastname).send_keys(input.lastname)
        driver.find_element(By.XPATH, elem.hps_id).clear()
        driver.find_element(By.XPATH, elem.id_empl).send_keys(input.id_empl)
        driver.find_element(By.XPATH, elem.btn_crt_lgn).click()
        driver.find_element(By.XPATH, elem.username).send_keys(input.username)
        driver.find_element(By.XPATH, elem.confirm_psw).send_keys(input.confir_pasw)
        driver.find_element(By.XPATH, elem.btn_save_add).click()
        validation = driver.find_element(By.XPATH, elem.status_empty_pass).text
        self.assertEqual(validation, "Required")

    def test_a_add_employee_Password_Confirm_NoMatch(self): #test cases 8
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_add_empl).click()
        driver.find_element(By.NAME, elem.firsname).send_keys(input.firstname)
        driver.find_element(By.NAME, elem.middle_name).send_keys(input.middlename)
        driver.find_element(By.NAME, elem.lastname).send_keys(input.lastname)
        driver.find_element(By.XPATH, elem.hps_id).clear()
        driver.find_element(By.XPATH, elem.id_empl).send_keys(input.id_empl)
        driver.find_element(By.XPATH, elem.btn_crt_lgn).click()
        driver.find_element(By.XPATH, elem.username).send_keys(input.username)
        driver.find_element(By.XPATH, elem.confirm_psw).send_keys("xxxxxxx")
        driver.find_element(By.XPATH, elem.btn_save_add).click()
        validation = driver.find_element(By.XPATH, elem.status_pasw_no_match).text
        self.assertEqual(validation, "Passwords do not match")

    def test_a_add_employee_empty_createLogin(self): #test cases 9
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baselogin.test_login(driver)
        driver.find_element(By.XPATH, elem.btn_PIM).click()
        driver.find_element(By.XPATH, elem.btn_add_empl).click()
        driver.find_element(By.NAME, elem.firsname).send_keys(input.firstname)
        driver.find_element(By.NAME, elem.middle_name).send_keys(input.middlename)
        driver.find_element(By.NAME, elem.lastname).send_keys(input.lastname)
        driver.find_element(By.XPATH, elem.hps_id).clear()
        driver.find_element(By.XPATH, elem.id_empl).send_keys(input.id_empl)
        driver.find_element(By.XPATH, elem.btn_crt_lgn).click()
        driver.find_element(By.XPATH, elem.btn_save_add).click()
        validation = driver.find_element(By.XPATH, elem.status_empty_pass).text
        self.assertEqual(validation, "Required")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_Add_Employee'))