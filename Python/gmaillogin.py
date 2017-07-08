import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dateutil.parser import parse

driver = webdriver.Firefox()
driver.get("http://gmail.com")
#assert "Python" in driver.title
elem = driver.find_element_by_id("Email")
elem.send_keys("vivekdixit213@gmail.com")
elem = driver.find_element_by_id("next")
elem.click()
elem = driver.find_element_by_id("Passwd")
elem.send_keys("Bangalore2050")
elem.click()
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.get('https://mail.google.com/mail/u/0/#inbox')

#elem = driver.find_elements_by_id("COMPOSE")
#elem = driver.find_element(By.XPATH, '//div[text()= "COMPOSE"]')

#driver.findElement(By.id("gbi4m1")).click();
#driver.findElement(By.id("gb_71")).click();

elem = driver.find_elements_by_xpath("gbi4m1")
elem.click()

elem = driver.find_element(By.XPATH, '//*[@id="gb_71"]')
elem.click()

#elem = driver.find_element_by_link_text("States, Regions & Branches")
#elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
#print elem
#elem.click()


driver.close()