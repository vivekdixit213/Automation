import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dateutil.parser import parse

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://localhost:8080")
#assert "Python" in driver.title
elem = driver.find_element_by_id("txtusername")
elem.send_keys("admin@arohan-test.esthenos.com")
elem = driver.find_element_by_id("txtpassword")
elem.send_keys("adminadmin")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.get('http://localhost:8080/admin/organisations')

elem = driver.find_element_by_link_text("Update")
#elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
print elem
elem.click()

#elem = driver.find_element_by_link_text("States, Regions & Branches")
#elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
#print elem
#elem.click()

elem = driver.find_element_by_link_text("Settings")
#elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
print elem
elem.click()






driver.close()