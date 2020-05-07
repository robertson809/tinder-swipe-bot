from selenium import webdriver
from time import sleep
from random import random

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        print('Accessing tinder.com')
        sleep(1)
        accept_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept_button.click()

        sleep(2)

        more_options_button = self.driver.find_element_by_xpath('// *[ @ id = "modal-manager"]/div/div/div/div/div[3]/span/button')
        more_options_button.click()

        sleep(2)
        try:
            print('Trying Facebook Login')
            fb_btn = self.driver.find_element_by_xpath('/ html / body / div[2] / div / div / div / div / div[3] / span / div[3] / button')
            fb_btn.click()
        except Exception:
            print('\"More Options\" button wasn\'t there, exiting to main page')
            close = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
            close.click()
            login_btn = bot.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            login_btn.click()
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            fb_btn.click()

        print('Beginning Facebook Login')
        sleep(.2)
        # # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        print('Facebook Login Complete')
        sleep(5)
        self.driver.switch_to.window(base_window)

        popup_1 = self.driver.find_element_by_xpath('/ html / body / div[2] / div / div / div / div / div[3] / button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

        print('Waiting for \"No Thanks\" to appear')
        sleep(5)
        try:
            no_thanks_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
            no_thanks_btn.click()
        except Exception:
            print('Guess quarentine\'s over')

        print("Login Complete")

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(2 - 1.5 * random())
            try:
                if random() > .13:
                    self.like()
                    print('Liked')
                else:
                    self.dislike()
                    print('Disliked')
            except Exception:
                sleep(1 - .8 * random())
                try:
                    self.close_popup()
                except Exception:
                    sleep(.2 - .1 * random())
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
print('Liking...')
sleep(1)
bot.like()
print('Disliking...')
sleep(1)
bot.dislike()
print('Auto-swiping')
bot.auto_swipe()
