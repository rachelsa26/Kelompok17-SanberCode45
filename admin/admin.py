import time
import unittest
import baseLogin
import baseAdmin
import HtmlTestRunner
from selenium import webdriver
from pageobject.data import inputan
from pageobject.locator import elem 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

class TestAdmin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_01_access_menu_admin(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        driver.find_element(By.XPATH, elem.menuAdminLoc).click()
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")

        # Validasi
        adminMenuValidation = driver.find_element(By.XPATH, elem.textSystemUsers).text
        self.assertEqual(adminMenuValidation, 'System Users')
    
    def test_02_search_user_by_username(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.usernameFilterLoc).send_keys(inputan.usernameAdmin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSearchLoc).click()
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")

    def test_03_search_user_by_wrong_username(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.usernameFilterLoc).send_keys(inputan.usernameLoginFailed)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSearchLoc).click()
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")
        time.sleep(3)
    
    def test_04_search_user_by_userrole_admin(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userroleFiterLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userroleAdminLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSearchLoc).click()
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")
        time.sleep(3)

        # Validasi
        validation = driver.find_element(By.XPATH, elem.textAdminSearchUserRoleLoc).text
        time.sleep(1)
        self.assertEqual(validation, inputan.textAdminValidation)
    
    def test_05_search_user_by_userrole_ess(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userroleFiterLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userroleESSLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSearchLoc).click()
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")
        time.sleep(3)

        # Validasi
        validation = driver.find_element(By.XPATH, elem.textESSSearchUserRoleLoc).text
        time.sleep(1)
        self.assertEqual(validation, inputan.textESSValidation)

    def test_06_search_user_by_employee_name(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.employeeNameFilterLoc).send_keys("A")
        time.sleep(10)
        driver.find_element(By.XPATH, elem.employeeNameDropDownFirstLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSearchLoc).click()
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")
        time.sleep(3)


    def test_07_search_user_by_wrong_employee_name(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.employeeNameFilterLoc).send_keys(inputan.usernameLoginFailed)
        time.sleep(5)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")
        time.sleep(3)

    def test_08_search_user_by_status_enabled(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusFilterLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusEnabledFilterLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSearchLoc).click()
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")
        time.sleep(1)

    
    def test_09_search_user_by_status_disabled(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusFilterLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusDisabledFilterLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSearchLoc).click()
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")
        time.sleep(1)
    
    def test_10_reset_filter(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.usernameFilterLoc).send_keys(inputan.usernameAdmin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userroleFiterLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userroleAdminLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.employeeNameFilterLoc).send_keys("A")
        time.sleep(5)
        driver.find_element(By.XPATH, elem.employeeNameDropDownFirstLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusFilterLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusDisabledFilterLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonReset).click()
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")
        time.sleep(1)

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportAdminUser'))