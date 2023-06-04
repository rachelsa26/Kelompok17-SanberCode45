import unittest
import time
import baselogin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pageobject.data import inputan
from random import randint
from pageobject.locator import elemen
import HtmlTestRunner

class TestEditUser(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())


    # def test_success_add_org_loc(self): #test success edit users at admin
    #     username = "".join([chr(randint(65, 90)) for _ in range(randint(6, 12))])
    #     driver = self.browser
    #     driver.implicitly_wait(20)
    #     driver.get(inputan.baseUrl)
    #     baselogin.test_login(driver)
    #     driver.find_element(By.XPATH,elemen.admin).click() 
    #     driver.find_element(By.XPATH,elemen.organization).click() 
    #     driver.find_element(By.XPATH,elemen.location).click() 
    #     driver.find_element(By.XPATH,elemen.loc_button).click() 
    #     driver.find_element(By.XPATH,elemen.name_loc).send_keys(username) 
    #     driver.find_element(By.XPATH,elemen.city_loc).send_keys("jogja") 
    #     driver.find_element(By.XPATH,elemen.prov_loc).send_keys("DIY") 
    #     driver.find_element(By.XPATH,elemen.post_loc).send_keys("55160") 
    #     driver.find_element(By.XPATH,elemen.whole_country).click()
    #     driver.find_element(By.XPATH,elemen.country_loc).click() 
    #     driver.find_element(By.XPATH,elemen.phone_loc).send_keys("0813677638") 
    #     driver.find_element(By.XPATH,elemen.fax_loc).send_keys("123141") 
    #     driver.find_element(By.XPATH,elemen.notes).send_keys("pasti berhasil") 
    #     driver.find_element(By.XPATH,elemen.address_loc).send_keys("jalan tamansiswa") 
    #     driver.find_element(By.XPATH,elemen.but_loc).click()
        
    #     time.sleep(5)


    # def test_failed_empty_org_loc_name(self): #test success edit users at admin
    #     driver = self.browser
    #     driver.implicitly_wait(20)
    #     driver.get(inputan.baseUrl)
    #     baselogin.test_login(driver)
    #     driver.find_element(By.XPATH,elemen.admin).click() 
    #     driver.find_element(By.XPATH,elemen.organization).click() 
    #     driver.find_element(By.XPATH,elemen.location).click() 
    #     driver.find_element(By.XPATH,elemen.loc_button).click() 
    #     # driver.find_element(By.XPATH,elemen.name_loc).send_keys("k17") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.city_loc).send_keys("jogja") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.prov_loc).send_keys("DIY") 
    #     driver.find_element(By.XPATH,elemen.post_loc).send_keys("55160") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.whole_country).click()
    #     driver.find_element(By.XPATH,elemen.country_loc).click() 
    #     driver.find_element(By.XPATH,elemen.phone_loc).send_keys("0813677638") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.fax_loc).send_keys("123141") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.notes).send_keys("pasti berhasil") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.address_loc).send_keys("jalan tamansiswa") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.but_loc).click()
        
    #     time.sleep(10)

    #     validation = driver.find_element(By.XPATH, elemen.err_nameloc).text
    #     self.assertEqual(validation, "Required")


    # def test_failed_empty_org_loc_country(self): #test success edit users at admin
    #     username = "".join([chr(randint(65, 90)) for _ in range(randint(6, 12))])
    #     driver = self.browser
    #     driver.implicitly_wait(20)
    #     driver.get(inputan.baseUrl)
    #     baselogin.test_login(driver)
    #     driver.find_element(By.XPATH,elemen.admin).click() 
    #     driver.find_element(By.XPATH,elemen.organization).click() 
    #     driver.find_element(By.XPATH,elemen.location).click() 
    #     driver.find_element(By.XPATH,elemen.loc_button).click() 
    #     driver.find_element(By.XPATH,elemen.name_loc).send_keys(username) 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.city_loc).send_keys("jogja") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.prov_loc).send_keys("DIY") 
    #     driver.find_element(By.XPATH,elemen.post_loc).send_keys("55160") 
    #     time.sleep(2)
    #     # driver.find_element(By.XPATH,elemen.whole_country).click()
    #     # driver.find_element(By.XPATH,elemen.country_loc).click() 
    #     driver.find_element(By.XPATH,elemen.phone_loc).send_keys("0813677638") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.fax_loc).send_keys("123141") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.notes).send_keys("pasti berhasil") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.address_loc).send_keys("jalan tamansiswa") 
    #     time.sleep(2)
    #     driver.find_element(By.XPATH,elemen.but_loc).click()
        
    #     time.sleep(10)

    #     validation = driver.find_element(By.XPATH, elemen.err_countryloc).text
    #     self.assertEqual(validation, "Required")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='ReportAddlocOrganization'))