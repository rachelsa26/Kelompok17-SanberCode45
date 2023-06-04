import time
import unittest
import baseLogin
import HtmlTestRunner
from selenium import webdriver
from PageObject.data import inputan
from PageObject.locator import elem 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_1_login_success(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/dashboard/index")

        # Validasi
        loginValidation = driver.find_element(By.XPATH, elem.textDashboadLoc).text
        self.assertEqual(loginValidation, 'Dashboard')
    
    def test_2_login_failed_wrong_username(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.NAME, "username").send_keys(inputan.usernameLoginFailed)
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(inputan.passwordLogin)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonLoginLoc).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/auth/login")

        # Validasi
        loginValidation = driver.find_element(By.XPATH, elem.textInvalidCredentialsLoc).text
        self.assertEqual(loginValidation, 'Invalid credentials')

    def test_3_login_failed_wrong_password(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.NAME, "username").send_keys(inputan.usernameAdmin)
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(inputan.passwordLoginFailed)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonLoginLoc).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/auth/login")

        # Validasi
        loginValidation = driver.find_element(By.XPATH, elem.textInvalidCredentialsLoc).text
        self.assertEqual(loginValidation, 'Invalid credentials')
    
    def test_4_login_failed_wrong_username_password(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.NAME, "username").send_keys(inputan.usernameLoginFailed)
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(inputan.passwordLoginFailed)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonLoginLoc).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/auth/login")

        # Validasi
        loginValidation = driver.find_element(By.XPATH, elem.textInvalidCredentialsLoc).text
        self.assertEqual(loginValidation, 'Invalid credentials')
    
    def test_5_login_failed_empty_username(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.NAME, "username").send_keys("")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(inputan.passwordLoginFailed)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonLoginLoc).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/auth/login")

        # Validasi
        loginValidation = driver.find_element(By.XPATH, elem.textRequiredUsernameLoc).text
        self.assertEqual(loginValidation, 'Required')
    
    def test_6_login_failed_empty_password(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.NAME, "username").send_keys(inputan.usernameAdmin)
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonLoginLoc).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/auth/login")

        # Validasi
        loginValidation = driver.find_element(By.XPATH, elem.textRequiredPasswordLoc).text
        self.assertEqual(loginValidation, 'Required')
    
    def test_7_login_failed_empty_username_password(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.NAME, "username").send_keys("")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("")
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonLoginLoc).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/auth/login")

        # Validasi
        loginValidation = driver.find_element(By.XPATH, elem.textRequiredPasswordLoc).text
        self.assertEqual(loginValidation, 'Required')
    
    def test_8_logout_success(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        time.sleep(1)
        baseLogin.test_success_login(driver)
        time.sleep(5)
        driver.find_element(By.XPATH, elem.profile).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonLogout).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/auth/login")

        # Validasi
        loginValidation = driver.find_element(By.XPATH, elem.textLogin).text
        self.assertEqual(loginValidation, 'Login')
    

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportLoginLogout'))
