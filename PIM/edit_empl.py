import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baseAdd
from PageObject.locator import elem
from PageObject.dataInput import input
import HtmlTestRunner

class TestEditEmployee(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_Success_edit_employee(self): #test cases 1
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baseAdd.test_a_Success_add_employee(driver)
        driver.find_element(By.XPATH, elem.btn_empl_list).click()
        driver.find_element(By.XPATH, elem.search_empl_name).send_keys(input.search)
        driver.find_element(By.XPATH, elem.btn_search).click()
        driver.find_element(By.XPATH, elem.btn_pencil).click()
        driver.find_element(By.XPATH, elem.btn_contrac_details).click()
        driver.find_element(By.XPATH, elem.address).send_keys(input.address)
        driver.find_element(By.XPATH, elem.number_hp).send_keys(input.number_hp)
        driver.find_element(By.XPATH, elem.email).send_keys(input.email)
        driver.find_element(By.XPATH, elem.btn_save_edit).click()
        driver.find_element(By.XPATH, elem.btn_job).click()
        driver.find_element(By.XPATH, elem.dropdown).click()
        driver.find_element(By.XPATH, elem.job_title).click()
        driver.find_element(By.XPATH, elem.btn_save_job).click()

    def test_a_Invalid_Email_Employee(self): #test cases 3
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baseAdd.test_a_Success_add_employee(driver)
        driver.find_element(By.XPATH, elem.btn_empl_list).click()
        driver.find_element(By.XPATH, elem.search_empl_name).send_keys(input.search)
        driver.find_element(By.XPATH, elem.btn_search).click()
        driver.find_element(By.XPATH, elem.btn_pencil).click()
        driver.find_element(By.XPATH, elem.btn_contrac_details).click()
        driver.find_element(By.XPATH, elem.address).send_keys(input.address)
        driver.find_element(By.XPATH, elem.number_hp).send_keys(input.number_hp)
        driver.find_element(By.XPATH, elem.email).send_keys("xxxxx@gmail.com")
        driver.find_element(By.XPATH, elem.btn_save_edit).click()
        driver.find_element(By.XPATH, elem.btn_job).click()
        driver.find_element(By.XPATH, elem.dropdown).click()
        driver.find_element(By.XPATH, elem.job_title).click()
        driver.find_element(By.XPATH, elem.btn_save_job).click()

    def test_a_Invalid_Number_Mobile(self): #test cases 4
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baseAdd.test_a_Success_add_employee(driver)
        driver.find_element(By.XPATH, elem.btn_empl_list).click()
        driver.find_element(By.XPATH, elem.search_empl_name).send_keys(input.search)
        driver.find_element(By.XPATH, elem.btn_search).click()
        driver.find_element(By.XPATH, elem.btn_pencil).click()
        driver.find_element(By.XPATH, elem.btn_contrac_details).click()
        driver.find_element(By.XPATH, elem.address).send_keys(input.address)
        driver.find_element(By.XPATH, elem.number_hp).send_keys("uuuuuuu")
        driver.find_element(By.XPATH, elem.email).send_keys(input.email)
        driver.find_element(By.XPATH, elem.btn_save_edit).click()
        driver.find_element(By.XPATH, elem.btn_job).click()
        driver.find_element(By.XPATH, elem.dropdown).click()
        driver.find_element(By.XPATH, elem.job_title).click()
        driver.find_element(By.XPATH, elem.btn_save_job).click()

    def test_a_Clear_All_Fields(self): #test cases 5
        driver = self.browser
        driver.implicitly_wait(15)
        driver.get(input.baseUrl)
        baseAdd.test_a_Success_add_employee(driver)
        driver.find_element(By.XPATH, elem.btn_empl_list).click()
        driver.find_element(By.XPATH, elem.search_empl_name).send_keys(input.search)
        driver.find_element(By.XPATH, elem.btn_search).click()
        driver.find_element(By.XPATH, elem.btn_pencil).click()
        driver.find_element(By.XPATH, elem.btn_save_clear).click()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report_Edit_Employee'))