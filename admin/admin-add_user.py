import time
import unittest
import baseLogin
import baseAdmin
import baseAddUser
import HtmlTestRunner
from selenium import webdriver
from pageobject.data import inputan
from pageobject.locator import elem
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

class TestAddUser(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_01_acces_add_user_feature(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        baseAddUser.test_add_button(driver)
        time.sleep(1)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/saveSystemUser")
        time.sleep(5)

        # Validasi
        validation = driver.find_element(By.XPATH, elem.textAddUserLoc).text
        self.assertEqual(validation, 'Add User')
    
    def test_02_add_user_success(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        baseAddUser.test_add_button(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAdminAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys("ce")
        time.sleep(10)
        driver.find_element(By.XPATH, elem.employeeNameDropdownFirstLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.statusEnabledAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.usernameAddUserLoc).send_keys("ceci.bo")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passwordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPasswordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSave).click()
        time.sleep(15)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/viewSystemUsers")
        time.sleep(5)
    
    def test_03_add_user_fail_mising_userrole(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        baseAddUser.test_add_button(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys("G")
        time.sleep(10)
        driver.find_element(By.XPATH, elem.employeeNameDropdownFirstLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.statusEnabledAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.usernameAddUserLoc).send_keys("Dray.cay")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passwordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPasswordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSave).click()
        time.sleep(10)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/saveSystemUser")
        time.sleep(5)

        # Validasi
        validation = driver.find_element(By.XPATH, elem.textRequiredUserRoleAddUserLoc).text
        self.assertEqual(validation, "Required")
    
    def test_04_add_user_fail_mising_employee_name(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        baseAddUser.test_add_button(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAdminAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.statusEnabledAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.usernameAddUserLoc).send_keys("Dray.cay")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passwordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPasswordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSave).click()
        time.sleep(10)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/saveSystemUser")
        time.sleep(5)

        # Validasi
        validation = driver.find_element(By.XPATH, elem.textRequiredEmployeeNameAddUserLoc).text
        self.assertEqual(validation, "Required")

    def test_05_add_user_fail_mising_status(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        baseAddUser.test_add_button(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAdminAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys("A")
        time.sleep(10)
        driver.find_element(By.XPATH, elem.employeeNameDropdownFirstLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.usernameAddUserLoc).send_keys("DrAy.cay")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passwordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPasswordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSave).click()
        time.sleep(10)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/saveSystemUser")
        time.sleep(5)

        # Validasi
        validation = driver.find_element(By.XPATH, elem.textRequiredStatusAddEmployeeLoc).text
        self.assertEqual(validation, "Required")

    def test_06_add_user_fail_mising_username(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        baseAddUser.test_add_button(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAdminAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys("G")
        time.sleep(10)
        driver.find_element(By.XPATH, elem.employeeNameDropdownFirstLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.statusEnabledAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.passwordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPasswordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSave).click()
        time.sleep(10)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/saveSystemUser")
        time.sleep(5)

        # Validasi
        validation = driver.find_element(By.XPATH, elem.textRequiredUsernameAddUserLoc).text
        self.assertEqual(validation, "Required")

    def test_07_add_user_fail_mising_password(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        baseAddUser.test_add_button(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAdminAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys("G")
        time.sleep(10)
        driver.find_element(By.XPATH, elem.employeeNameDropdownFirstLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.statusEnabledAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.usernameAddUserLoc).send_keys("Dray.cay")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.confirmPasswordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSave).click()
        time.sleep(10)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/saveSystemUser")
        time.sleep(5)

        # Validasi
        validation = driver.find_element(By.XPATH, elem.textRequiredPasswordAddUserLoc).text
        self.assertEqual(validation, "Required")
    
    def test_07_add_user_fail_mising_confirm_password(self):
        driver = self.driver
        time.sleep(1)
        driver.get(inputan.baseUrl)
        time.sleep(5)
        baseLogin.test_login(driver)
        time.sleep(5)
        baseAdmin.test_success_admin_menu(driver)
        time.sleep(1)
        baseAddUser.test_add_button(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.userRoleAdminAddUserLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.employeeNameAddUserLoc).send_keys("G")
        time.sleep(10)
        driver.find_element(By.XPATH, elem.employeeNameDropdownFirstLoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.statusAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.statusEnabledAddUserLoc).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.usernameAddUserLoc).send_keys("Dray.cay")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.passwordAddUserLoc).send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonSave).click()
        time.sleep(10)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/admin/saveSystemUser")
        time.sleep(5)

        # Validasi
        validation = driver.find_element(By.XPATH, elem.textRequiredConfirmPasswordAddUserLoc).text
        self.assertEqual(validation, "Required")

        
    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportAddUser'))
