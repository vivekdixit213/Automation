import os
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dateutil.parser import parse
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome("/home/vivek/Documents/Automate/chromedriver")

driver.maximize_window()
driver.get("https://testing.truweight.in/?allowpassword")
#assert "Python" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys("sonia@gmail.com")
elem = driver.find_element_by_id("password")
elem.send_keys("@2017truweight")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.get('http://localhost:8080/admin/organisations')
wait = WebDriverWait(driver, 10)

elem = driver.find_elements_by_xpath("//*[contains(text(), 'Update')]")[0]
print elem
#elem.click()

#elem = driver.find_element_by_link_text("Update")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'States, Regions & Branches')]")[0]
print elem
elem.click()

driver.get('http://localhost:8080/admin/organisations')
wait = WebDriverWait(driver, 10)

elem = driver.find_elements_by_xpath("//*[contains(text(), 'Update')]")[0]
print elem
elem.click()

#elem = driver.find_element_by_link_text("Update")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'Products')]")[0]
print elem
elem.click()

driver.get('http://localhost:8080/admin/organisations')
wait = WebDriverWait(driver, 10)

elem = driver.find_elements_by_xpath("//*[contains(text(), 'Update')]")[0]
print elem
elem.click()

#elem = driver.find_element_by_link_text("Update")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'Employees')]")[0]
print elem
elem.click()

driver.get('http://localhost:8080/admin/organisations')
wait = WebDriverWait(driver, 10)

#elem = driver.find_element_by_link_text("Update")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'Update')]")[0]
print elem
elem.click()

elem = driver.find_elements_by_xpath("//*[contains(text(), 'Upload APK')]")[0]
print elem
elem.click()

driver.get('http://localhost:8080/admin/organisations')
wait = WebDriverWait(driver, 10)

elem = driver.find_elements_by_xpath("//*[contains(text(), 'Update')]")[0]
print elem
elem.click()

#elem = driver.find_element_by_link_text("Update")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'Settings')]")[0]
print elem
elem.click()

driver.get('http://localhost:8080/admin/organisations')
wait = WebDriverWait(driver, 10)

elem = driver.find_elements_by_xpath("//*[contains(text(), 'Update')]")[0]
print elem
elem.click()

#elem = driver.find_element_by_link_text("Update")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'Manage Collections')]")[0]
print elem
elem.click()

driver.close()

driver = webdriver.Chrome("/home/vivek/Documents/Automation/Python/chromedriver")

driver.maximize_window()
driver.get("http://localhost:8080")
#assert "Python" in driver.title
elem = driver.find_element_by_id("txtusername")
elem.send_keys("admin@arohan-test2.esthenos.com")
elem = driver.find_element_by_id("txtpassword")
elem.send_keys("adminadmin")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.get('http://localhost:8080/admin/organisations')
wait = WebDriverWait(driver, 10)

elem = driver.find_elements_by_xpath("//*[contains(text(), 'Update')]")[0]
print elem
elem.click()

#elem = driver.find_element_by_link_text("Employees")
elem = driver.find_elements_by_xpath("//*[contains(text(), 'Upload APK')]")[0]
print elem
elem.click()

driver.find_element_by_css_selector('input[type="file"]').clear()

driver.find_element_by_css_selector('input[type="file"]').send_keys(r"/home/vivek/Downloads/Arohan 1.2.12 .apk")

elem = driver.find_element_by_xpath("//button[contains(text(),'Upload')]")
print elem
elem.click()

#elem = driver.find_element_by_link_text("apk_uploads/26072017.1751.apk")
#elem.click()