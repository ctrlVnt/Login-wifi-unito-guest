from fileinput import close
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class LogWifi:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://captive.wifi.unito.it/fs/customwebauth/login-01.html?switch_url=https://captive.wifi.unito.it/login.html&ap_mac=cc:db:93:0c:27:20&client_mac=74:12:b3:fd:b2:b3&wlan=unito-guest&redirect=detectportal.firefox.com/canonical.html')
        email_xpath = '/html/body/div[2]/div[2]/div/div/form/div[1]/input'
        password = '/html/body/div[2]/div[2]/div/div/form/div[2]/input'
        email = bot.find_element_by_xpath(email_xpath)
        email.send_keys(self.username)
        password = bot.find_element_by_xpath(password)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        bot.close()
        bot.close()
        
ed = LogWifi('user', 'password')
ed.login()