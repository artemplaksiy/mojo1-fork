from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

try:
    browser = webdriver.Chrome()
    browser.get("https://devlb.mojosells.com/crm/login/")
    wait = WebDriverWait(browser, 20)
    browser.implicitly_wait(20)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#submit")))
    # login into crm
    browser.find_element(By.CSS_SELECTOR, "input#id_username").clear()
    browser.find_element(By.CSS_SELECTOR, "input#id_username").send_keys("gabik")
    browser.find_element(By.CSS_SELECTOR, "input#id_password").clear()
    browser.find_element(By.CSS_SELECTOR, "input#id_password").send_keys("123gabik00t0r")
    browser.find_element(By.CSS_SELECTOR, "input#submit").click()
    time.sleep(5)


    pickle.dump(browser.get_cookies(), open('session_crm', 'wb'))
    time.sleep(3)

finally:
    browser.quit()