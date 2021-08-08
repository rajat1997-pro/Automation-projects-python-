from selenium import webdriver
import time


class Form:
    DRIVER_PATH = "c://development/chromedriver.exe"

    def __init__(self, url, data):
        self.driver = webdriver.Chrome(executable_path=self.DRIVER_PATH)
        self.driver.get(url=url)
        self.filling_fields(data)

    def filling_fields(self, data):
        list_of_dicts = data
        for i in range(len(data)):
            time.sleep(2)
            self.fill_address(list_of_dicts[i]["address"])
            self.fill_price(list_of_dicts[i]["price"])
            self.fill_link(list_of_dicts[i]["links"])
            self.submit()
            self.submit_another()

    def fill_address(self, address1):
        address = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address.send_keys(address1)

    def fill_price(self, price1):
        price = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price.send_keys(price1)

    def fill_link(self, link1):
        link = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link.send_keys(link1)

    def submit(self):
        submit_button = self.driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        submit_button.click()

    def submit_another(self):
        submit_button = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submit_button.click()
