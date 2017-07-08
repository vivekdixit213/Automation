import os
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dateutil.parser import parse


driver = webdriver.Chrome("/home/vivek/Documents/Automate Script files/chromedriver")

driver.maximize_window()
driver.get("http://arohan.esthenos.com")
#assert "Python" in driver.title
elem = driver.find_element_by_id("txtusername")
elem.send_keys("admin@arohan.esthenos.com")
elem = driver.find_element_by_id("txtpassword")
elem.send_keys("arohan@123")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.get('http://arohan.esthenos.com/admin/organisations')

elem = driver.find_element_by_link_text("Update")
#elem = driver.find_element(By.XPATH, '//button[text()="Update"]')
print elem
elem.click()

#elem = driver.find_element_by_link_text("States, Regions & Branches")
#elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
#print elem
#elem.click()

elem = driver.find_element_by_link_text("Employees")
#elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
print elem
elem.click()

#######UODATE EMP

with open('West_Bengal_Remaining_Emp.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
	    elem = driver.find_element_by_name("first_name_add_organisation")
	    # elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
	    elem.clear()
	    print elem
	    elem.send_keys(row[1].split(' ')[0].strip())

	    elem = driver.find_element_by_name("last_name_add_organisation")
	    # elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
	    elem.clear()
	    print elem
	    elem.send_keys(''.join(row[1].split(' ')[1:]).strip())

	    elem = driver.find_element_by_name("email_add_organisation")
	    # elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
	    print elem
	    elem.clear()
	    elem.send_keys(row[0] + '@arohan.esthenos.com')

	    elem = driver.find_element_by_name("id_add_organisation")
	    elem.clear()
	    elem.send_keys(row[0])

	    elem = driver.find_element_by_name("password_add_organisation")
	    # elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
	    print elem
	    elem.clear()
	    elem.send_keys(row[0])

	    elem = driver.find_element_by_name("date_of_joining")
	    # elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
	    print elem
	    elem.clear()
	    elem.send_keys(parse(row[6]).strftime("%m/%d/%Y"))

	    elem = driver.find_element_by_name("valid_email_add_organisation")
	    print elem
	    elem.clear()
	    elem.send_keys(row[0] + '@gmail.com')

	    elem = driver.find_element_by_name("address_add_org_emp")
	    elem.clear()
	    elem.send_keys(row[4])

	    element = driver.find_element_by_xpath("//select[@name='country_add_organisation']")
	    print "ELE", element
	    all_options = element.find_elements_by_tag_name("option")
	    selcted_op = all_options[105]
	    selcted_op.click()

	    element = driver.find_element_by_xpath("//select[@name='state_add_organisation']")
	    print "ELE	", element
	    all_options = element.find_elements_by_tag_name("option")
	    selcted_op = all_options[len(all_options) - 1]
	    selcted_op.click()

	    # element = driver.find_element_by_xpath("//select[@name='role']")
	    # print "ELE", element
	    # all_options = element.find_elements_by_tag_name("option")
	    # selcted_op = all_options[len(all_options) - 1]
	    # selcted_op.click()

	    element = driver.find_element_by_xpath("//select[@name='role']")
	    print "ELE	", element
	    all_options = element.find_elements_by_tag_name("option")

	    if row[2] == 'Branch Head':
		    print "BM : ", row
		    selcted_op = all_options[len(all_options) - 2]
		    selcted_op.click()
	    elif row[2] == 'Customer Service Representative':
		    print "CSR : ", row
		    selcted_op = all_options[len(all_options) - 1]
		    selcted_op.click()

	    elem = driver.find_element_by_name("city_add_organisation")
	    # elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
	    elem.clear()
	    print elem
	    elem.send_keys(row[4])

	    elem = driver.find_element_by_name("postal_code_add_organisation")
	    # elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
	    elem.clear()
	    print elem
	    elem.send_keys("560074")

	    elem = driver.find_element_by_name("tele_code_add_organisation")
	    # elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
	    elem.clear()
	    print elem
	    elem.send_keys("91")

	    elem = driver.find_element_by_name("teleno_add_organisation")
	    # elem = driver.find_element(By.XPATH, '//button[text()="Upadte"]')
	    elem.clear()
	    print elem
	    elem.send_keys(row[7])

	    # elem = driver.find_element_by_css_selector('btn btn-small btn-danger btn-cons')#d
	    elem = driver.find_element_by_xpath("//button[contains(text(),'Add Employee')]")
	    print elem
	    #elem.click()