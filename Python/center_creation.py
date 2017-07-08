import os
import unittest
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import math
import csv
import sys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dateutil.parser import parse

driver = webdriver.Chrome("/home/vivek/Documents/Automate Script files/chromedriver")

driver.maximize_window()

driver.get("http://arohan-test2.esthenos.com")
#assert "Python" in driver.title
elem = driver.find_element_by_id("txtusername")
elem.send_keys("admin@arohan-test2.esthenos.com")
elem = driver.find_element_by_id("txtpassword")
elem.send_keys("adminadmin")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.get('http://arohan-test2.esthenos.com/centers/manage')

time.sleep(5)

elem = driver.find_element_by_xpath("//*[text()='Center Manager']")
elem = driver.find_element_by_xpath("//*[text()='Vivek Dixit']")
#elem.send_keys(Keys.RETURN)

time.sleep(5)

elem = driver.find_element_by_id('new-center')
elem.send_keys("July 02")
elem.send_keys(Keys.RETURN)
#elem.click()



