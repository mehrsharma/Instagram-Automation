from selenium import webdriver
import os
import configparser
import time
username = '#'
password = '#'

class InstagramBot:
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver')
        self.login()

    def login(self): 
        self.driver.get('https://www.instagram.com/')
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
        time.sleep(2)
    def nav_user(self):
        self.driver.get('https://www.instagram.com/mehrsharma_/')
        time.sleep(10)
    def following(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[2]/a').click()

        
if __name__ == '__main__':
    ig_bot = InstagramBot(username, password)
    ig_bot.nav_user()
    ig_bot.following()
