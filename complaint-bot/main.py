from InternetSpeed import InternetSpeedTwitterBot
PROMISED_DOWN = 100
PROMISED_UP = 100
TWITTER_USERNAME = "RajatShekh1997"
TWITTER_PASSWORD = "GRf$Er@T|6o+YU1"

bot = InternetSpeedTwitterBot()


bot.get_internet_speed()
if bot.CURRENT_DOWN_SPEED < 75.00 or bot.CURRENT_UPLOAD_SPEED < 50.00:
    bot.tweet_at_provider(user_name=TWITTER_USERNAME, password=TWITTER_PASSWORD, promised_up=PROMISED_UP,
                          promised_down=PROMISED_DOWN)
else:
    print("service is fine")

