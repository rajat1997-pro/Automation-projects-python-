import requests
from pprint import pprint
from bs4 import BeautifulSoup
import smtplib

user_name = "princeshekhawat921@gmail.com"
password = "PRINCE1997"

PRODUCT_URL = "https://www.amazon.in/dp/B08N5WRWNW/ref=fs_a_mn_2?th=1"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
LANGUAGE = "en-US,en;q=0.9"
char_set = "utf-8"

request_line = "GET / HTTP/1.1"
accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
ip = "47.31.139.32"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": LANGUAGE,
    "Accept-Charset": char_set,
    "Upgrade-Insecure-Requests": "1",
    "Request Line": request_line,
    "Accept": accept,
    "X-Http-Proto": "HTTP/1.1",
    "X-Real-Ip": ip,
}

response = requests.get(url=PRODUCT_URL, headers=headers).text


# pprint(response)
def convert_to_float(price):
    try:
        st = float(price)

    except ValueError:
        st = " "
        price_list = price.split(",")
        for n in price_list:
            st = st + n

    return float(st)


def send_email(name, l_price, link):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_name, password=password)
        connection.sendmail(from_addr=user_name,
                            to_addrs="rajatshekhawat38@gmail.com",
                            msg=f"subject:Buy Alert\n\n{name} is now ₹{l_price}\n{link}".encode('utf-8'))


soup = BeautifulSoup(response, "lxml")

# for product name
name_span = soup.find("span", class_="a-size-large product-title-word-break")
name = name_span.get_text()

# for price
price_span = soup.find("span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price_text = price_span.get_text()

price_in_string = price_text.split("₹")[1]
price = convert_to_float(price=price_in_string)
if price < 130000.00:
    send_email(name=name, l_price=price, link=PRODUCT_URL)

