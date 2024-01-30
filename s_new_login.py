from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)

    #browser.get("https://app31.mojosells.com/home/")
    #browser.get("https://app31.mojosells.com/home/")
    #time.sleep(5)

    for cookie in pickle.load(open('session', 'rb')):
        print(cookie)
        if cookie['name'] == "sessionid" and cookie['domain'] == "app31.mojosells.com":
            browser.add_cookie(cookie)
        #browser.add_cookie(cookie)

    print('cookies loaded')
    time.sleep(5)
    browser.get("https://app31.mojosells.com/home/")
    #browser.refresh()
    time.sleep(5)

finally:
    browser.quit()