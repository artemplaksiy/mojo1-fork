from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

try:
    browser = webdriver.Chrome()
    browser.get("https://lb11.mojosells.com/login/")
    browser.implicitly_wait(20)

    # login
    email_input = browser.find_element(By.XPATH, '//input[@name="email"]')
    email_input.clear()
    email_input.send_keys("g.torosyan@g-sg.net")

    password_input = browser.find_element(By.XPATH, '//input[@name="password"]')
    password_input.clear()
    password_input.send_keys("password1")

    time.sleep(3)
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(15)
    #Assert Home Page
    #news_title = browser.find_element(By.CSS_SELECTOR, "div.HomeView_newsTitle__VgBZL")
    #assert news_title.text in "News:", "something wrong with home page's title"
    #time.sleep(3)

    pickle.dump(browser.get_cookies(), open('session', 'wb'))
    time.sleep(5)

finally:
    browser.quit()



