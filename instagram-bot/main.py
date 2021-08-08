from instagram import InstaFollower
USER_NAME = "SOKSAN1996"
PASSWORD = "PRINCE1997"

CHROME_DRIVER_PATH = "c://development/chromedriver.exe"
account = "lanarhoades"

insta = InstaFollower(CHROME_DRIVER_PATH)
insta.login(user=USER_NAME, password=PASSWORD)
insta.find_followers(account=account)
# insta.follow()


