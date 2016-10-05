'''
Created on Oct 5, 2016

@author: Vivek Dixit
'''
import os
from selenium import webdriver

chromedriver = "/Users/adam/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.quit()