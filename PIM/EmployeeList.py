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

class TestSearchEmployeeList():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_searchEmployeeList(self):
    # Test name: Search Employee List
    # Step # | name | target | value
    # 1 | open | /web/index.php/pim/viewEmployeeList | 
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    # 2 | setWindowSize | 1552x880 | 
    self.driver.set_window_size(1552, 880)
    # 3 | click | css=.oxd-autocomplete-text-input--focus > input | 
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input--focus > input").click()
    # 4 | type | css=.oxd-autocomplete-text-input--focus > input | David  Morris
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input--focus > input").send_keys("David  Morris")
    # 5 | mouseUp | css=.oxd-grid-item:nth-child(5) .oxd-input-group__label-wrapper | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-grid-item:nth-child(5) .oxd-input-group__label-wrapper")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
  
