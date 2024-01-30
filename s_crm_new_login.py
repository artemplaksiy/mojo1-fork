from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)

    browser.get("https://devlb.mojosells.com/crm/login/")
    #browser.get("https://app31.mojosells.com/home/")
    #time.sleep(5)

    for cookie in pickle.load(open('session_crm', 'rb')):
        browser.add_cookie(cookie)

    print('cookies loaded')
    time.sleep(5)
    browser.get("https://devlb.mojosells.com/crm/home/")
    #browser.refresh()
    time.sleep(15)

finally:
    browser.quit()