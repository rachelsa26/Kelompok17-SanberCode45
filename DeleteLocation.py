import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDELETELOCATION():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dELETELOCATION(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations")
    self.driver.set_window_size(1552, 880)
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(2) .oxd-icon-button:nth-child(1) > .oxd-icon").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(2) .oxd-icon-button:nth-child(1) > .oxd-icon")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--label-danger").click()
  
