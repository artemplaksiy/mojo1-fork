from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_nhs_street():
    try:
        browser = webdriver.Chrome()
        browser.get("https://lb11.mojosells.com/login/")
        wait = WebDriverWait(browser, 15)
        browser.implicitly_wait(15)

        # login
        email_input = browser.find_element(By.XPATH, '//input[@name="email"]')
        email_input.clear()
        email_input.send_keys("g.torosyan@g-sg.net")

        password_input = browser.find_element(By.XPATH, '//input[@name="password"]')
        password_input.clear()
        password_input.send_keys("password1")

        browser.find_element(By.XPATH, '//button[@type="submit"]').click()

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.HomeView_newsTitle__VgBZL")))

        #go to DataDialer
        browser.find_element(By.XPATH, '//img[@alt="Data & Dialer"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.Table_bottomActionsAndPaginationContainer__2LZDu")))

        # go to NHS
        browser.find_element(By.XPATH, '//img[@src="/static/media/neighborhood-search.1fa92d65.svg"]').click()




