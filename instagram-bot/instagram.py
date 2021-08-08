from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self, user, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        user_name = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(user)

        Password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        Password.send_keys(password)
        Password.send_keys(Keys.ENTER)

    def find_followers(self, account):
        time.sleep(4)
        self.driver.get("https://www.instagram.com/lanarhoades/")
        followers_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_button.click()
        time.sleep(4)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        accounts = self.driver.find_elements_by_css_selector(".isgrP li button")
        print(accounts)
        for i in range(len(accounts)):
            try:
                accounts[i].click()
            except ElementClickInterceptedException:
                cancel = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel.click()
            time.sleep(2)
