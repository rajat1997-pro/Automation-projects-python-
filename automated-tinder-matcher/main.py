import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

E_MAIL = "rajatshekhawat38@gmail.com"
PASSWORD = "PRINCE1997"

driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)
# login with facebook

driver.get("https://tinder.com")
time.sleep(4)
login_button = driver.find_element_by_xpath(
    '//*[@id="o-738591094"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login_button.click()
time.sleep(2)
try:
    facebook_button = driver.find_element_by_xpath(
        '//*[@id="o1827995126"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')

except NoSuchElementException:
    print("exception facebook")
    more = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div[1]/div/div[3]/span/button')
    more.click()
    facebook_button = driver.find_element_by_xpath(
        '//*[@id="o1827995126"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
facebook_button.click()
time.sleep(2)
list = driver.window_handles
base_window = driver.window_handles[0]
try:
    fb_window = driver.window_handles[1]
except IndexError:
    time.sleep(10)
    try:
        fb_window = driver.window_handles[1]
    except IndexError:
        time.sleep(2)
        fb_window = driver.window_handles[1]

driver.switch_to.window(fb_window)

time.sleep(2)
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys(E_MAIL)
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
time.sleep(3)
try:
    loaction_allow = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div/div/div[3]/button[1]/span')
except NoSuchElementException:
    print("location")
    time.sleep(4)
    loaction_allow = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div/div/div[3]/button[1]/span')
loaction_allow.click()
notification = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div/div/div[3]/button[2]/span')
notification.click()

not_100 = True
count = 0
while not_100:
    if count == 100:
        not_100 = False
    time.sleep(10)
    try:
        like_button = driver.find_element_by_css_selector('driver.find_element_by_css_selector(".Mx(a):nth-child(2) path")')
    except NoSuchElementException:
        like_button = driver.find_element_by_css_selector('driver.find_element_by_css_selector(".Mx(a):nth-child(2) path")')
    like_button.click()
    count += 1
