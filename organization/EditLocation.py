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

class TestNegativeEditLocation():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_negativeEditLocation(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLocations")
    self.driver.set_window_size(1552, 880)
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-icon-button:nth-child(2) > .oxd-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-select-text-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
  
