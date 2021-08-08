from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    CURRENT_DOWN_SPEED = None
    CURRENT_UPLOAD_SPEED = None

    def __init__(self):
        CHROME_DRIVER_PATH = "C:\development\chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(70)
        down_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        up_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.CURRENT_DOWN_SPEED = float(down_speed.text)
        self.CURRENT_UPLOAD_SPEED = float(up_speed.text)

    def tweet_at_provider(self, user_name, password, promised_down, promised_up):
        self.driver.get("https://twitter.com/?logout=1627882211702")
        time.sleep(2)
        login = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[3]/span/span')
        login.click()
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span')
        login_button.click()
        login_email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        login_email.send_keys(user_name)
        login_password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        login_password.send_keys(password)
        login_password.send_keys(Keys.ENTER)
        time.sleep(5)
        message_box = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        message_box.send_keys(f"Hey @excitel_rocks, why is my internet speed {self.CURRENT_DOWN_SPEED}down"
                              f"/{self.CURRENT_UPLOAD_SPEED}up when i pay for {promised_down}down/{promised_up}up?")

        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()



