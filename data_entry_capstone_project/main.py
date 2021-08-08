from scraping_data import Scraper
from filling_form import Form
from pprint import pprint

SOURCE_DATA_URL = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.53907240820313%2C%22east%22%3A-122.32758559179688%2C%22south%22%3A37.70347954028636%2C%22north%22%3A37.84703368102794%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A1235192%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfRO-dqnp7f0MAM7A_JlXchNkkIACu3rhN3iuk1NIm5pXddaw/viewform?usp=sf_link"

scrape = Scraper(zillow_url=SOURCE_DATA_URL)
links = scrape.links_list()
address = scrape.names_list()
prices = scrape.price_list()
combined_data = [{"address": address[i],
                  "price": prices[i],
                  "links": links[i]} for i in range(len(links))]

form = Form(GOOGLE_FORM, data=combined_data)
