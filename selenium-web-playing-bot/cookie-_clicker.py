import selenium.common.exceptions
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
money = driver.find_element_by_id("money")

cursor_button = driver.find_element_by_id("buyCursor")

time_out = time.time() + 5

five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > time_out:
        # getting list of all items
        store_list = driver.find_elements_by_css_selector("#store b")

        cost_list1 = [item.text.split("-")[1] for item in store_list[:8]]
        # print(cost_list1)
        cost_list2 = []
        for i in cost_list1:
            if "," in i:
                i = i.replace(",", "")
            i = i.strip()
            cost_list2.append(int(i))
        # print(cost_list2)

        affordable_list = []
        for i in cost_list2:

            money = driver.find_element_by_id("money").text
            if "," in money:
                money1 = money.replace(",", "")
                money1 = int(money1.strip())
            else:
                money1 = int(money)

            if i < money1:
                affordable_list.append(i)
        index_value = affordable_list.index(min(affordable_list))
        store_list[index_value].click()
        time_out = time.time() + 5

    if time.time() > five_min:
        print(driver.find_element_by_id("cps").text)
        break


