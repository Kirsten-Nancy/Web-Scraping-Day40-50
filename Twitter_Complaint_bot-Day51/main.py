import time
from selenium import webdriver

import config

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = config.TWITTER_EMAIL
TWITTER_PASSWORD = config.TWITTER_PASSWORD

chrome_driver_path = "C:\\Development\\chromedriver_win32\\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(30)

        #     cookies = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        #     cookies.click()
        #
        start_btn = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '1]/a/span[4]')
        start_btn.click()

        time.sleep(60)
        self.up = self.driver.find_element_by_class_name("download-speed").text
        print(self.up)
        self.down = self.driver.find_element_by_class_name("upload-speed").text
        print(self.down)


    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get('https://twitter.com/')
            self.driver.maximize_window()
            time.sleep(1)
            login_option = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div['
                                                             '1]/div[2]/div[3]/a[2]')
            login_option.click()

            time.sleep(1)
            username = self.driver.find_element_by_name("session[username_or_email]")
            username.send_keys(TWITTER_EMAIL)

            password = self.driver.find_element_by_name("session[password]")
            password.send_keys(TWITTER_PASSWORD)

            time.sleep(1)
            login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                          '2]/form/div/div[3]/div/div')
            login_btn.click()

            time.sleep(5)
            tweet = self.driver.find_element_by_class_name('public-DraftStyleDefault-block')
            tweet.send_keys(f'Hey ISP, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?')
            tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                          '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                          '4]/div/div/div[2]/div[3]')
            tweet_btn.click()

        else:
            print('Excellent speeds')
        self.driver.quit()



ispbot = InternetSpeedTwitterBot(chrome_driver_path)
ispbot.get_internet_speed()
ispbot.tweet_at_provider()
