import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

E_MAIL = "rajatshekhawat38@gmail.com"
PASSWORD = "jczE(4qW\:,:WF&"
driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
name = driver.find_element_by_id("username")
name.send_keys(E_MAIL)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=115918471&keywords=python%20developer&location=New%20Delhi%2C%20Delhi%2C%20India")
job_list = driver.find_element_by_css_selector(".job-card-list__title")
job_list.click()
button = driver.find_element_by_css_selector(".jobs-s-apply--fadein")
button.click()
# # no = driver.find_element_by_class_name("fb-single-line-text__input")
# # no.send_keys("9711443306")
submit = driver.find_element_by_css_selector("footer button")
submit.click()
