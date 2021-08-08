from selenium import webdriver
from pprint import pprint

chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

date_list = [driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i + 1}]/time').text
             for i in range(5)]

# print(date_list)

anchor_list = [driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i + 1}]/a').text
               for i in range(5)]

# print(anchor_list)

# create dictionary
events_dict = {i + 1: {"time": date_list[i],
               "name": anchor_list[i]} for i in range(5)}
pprint(events_dict)

driver.quit()
