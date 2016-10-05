


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver= webdriver.Firefox()
driver.get("http://mail.google.com")

time.sleep(5)

emailid=driver.find_element_by_id("Email")
emailid.send_keys("vivekflipkart213@gmail.com")
elem = driver.find_element_by_id("next")
elem.click()

time.sleep(5)

passw=driver.find_element_by_id("Passwd")
passw.send_keys("Bangalore2050")

time.sleep(5)

signin=driver.find_element_by_id("signIn")
signin.click()


time.sleep(5)


sentmail= driver.find_element_by_link_text('Sent Mail')
sentmail.click()


time.sleep(5)


lout= driver.find_element_by_link_text('Sign out')
lout.click()