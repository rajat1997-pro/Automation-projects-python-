from bs4 import BeautifulSoup
import requests


class Scraper:
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.9"

    def __init__(self, zillow_url):
        headers = {
            "User-Agent": self.USER_AGENT,
            "Accept-Language": self.LANGUAGE,
            "X-Real-Ip": "146.196.32.216",
            "X-Http-Proto": "HTTP/1.1",
        }
        response = requests.get(url=zillow_url, headers=headers)
        file = response.text
        self.soup = BeautifulSoup(file, "html.parser")

    def links_list(self):
        link_list_data = self.soup.select(selector=".list-card-top a")
        link_list = []
        for i in link_list_data:
            link_list.append(i.get("href"))
        for i in range(len(link_list)):

            if "/b" in link_list[i]:
                link_list[i] = link_list[i].replace("/b", "https://www.zillow.com/homedetails")
            link_list[i] = link_list[i]
        return link_list

    def names_list(self):
        names_data = self.soup.find_all(name="address", class_="list-card-addr")
        names_list = [name.getText() for name in names_data]
        return names_list

        # print(self.names_list)

    def price_list(self):
        price_data = self.soup.find_all(name="div", class_="list-card-price")
        price_list = [i.getText().split("/")[0] for i in price_data]
        return price_list
        # print(self.price_list)
