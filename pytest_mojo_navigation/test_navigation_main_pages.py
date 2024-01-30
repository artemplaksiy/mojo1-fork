from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_naviation_main_pages(browser):

    browser.get("https://lb11.mojosells.com/login/")
    wait = WebDriverWait(browser, 15)
    browser.implicitly_wait(15)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")))
    # login
    email_input = browser.find_element(By.XPATH, '//input[@name="email"]')
    email_input.clear()
    email_input.send_keys("g.torosyan@g-sg.net")

    password_input = browser.find_element(By.XPATH, '//input[@name="password"]')
    password_input.clear()
    password_input.send_keys("password1")

    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.HomeView_newsTitle__VgBZL")))

    # Assert Home Page
    join_webinar_button = browser.find_element(By.CSS_SELECTOR, "div.HomeView_textContent__2L3mx")
    assert join_webinar_button.text in "Join Webinar", "something wrong with home page"

    #Data Dialer
    browser.find_element(By.XPATH, '//img[@alt="Data & Dialer"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.Table_bottomActionsAndPaginationContainer__2LZDu")))
    #Asset for Data Dialer
    all_contacts_data_header = browser.find_element(By.CSS_SELECTOR, 'div.Generic_subtitle2__3FiOt')
    assert all_contacts_data_header.text in "All Contacts", "DataDialer page Error(header)"

    #Calendar
    browser.find_element(By.XPATH, '//img[@alt="Calendar"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.CalendarTableView_bottomActionBar__2TkCO")))
    #Assert for Calendar
    calendar_header = browser.find_element(By.CSS_SELECTOR, "div.Generic_subtitle2__3FiOt")
    #search_logo = browser.find_element(By.XPATH, '//img[@alt="search icon"]').is_displayed()
    assert calendar_header.text in "Calendar", "Calendar page Error(header)"

    #Reports. First Call Detail Report page
    browser.find_element(By.XPATH, '//img[@alt="Reports"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.CallDetailReportView_reportButtonsContainer__2_6Xg")))
    #Assert for Reports. First Call Detail Report page
    call_detail_report_header = browser.find_element(By.CSS_SELECTOR, "div.Generic_subtitle2__3FiOt")
    assert call_detail_report_header.text in "Call Detail Report", "Call Detail Report page Error(header)"

    #Leadstore
    browser.find_element(By.XPATH, '//img[@alt="Leadstore"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.LeadstoreHomeMainView_first__lOTQY")))
    #Assert for Leadstore
    leadstore_header = browser.find_element(By.CSS_SELECTOR, "div.Generic_subtitle2__3FiOt")
    assert leadstore_header.text in "Welcome To The Leadstore", "Leadstore page Error(header)"

    #Logout
    browser.find_element(By.CSS_SELECTOR, "div.Placeholder_caption__O4F-Z").click()
    browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_link__2RBsi").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")))
    #Assert login page
    login_page_header = browser.find_element(By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")
    assert login_page_header.text in "Sign In to Mojo", "Login page Error(header)"
    support_phone = browser.find_element(By.CSS_SELECTOR, "span.CallTollFree_CallTollFreePhone__3vqFR")
    assert support_phone.text in "877-859-6656", "Login page Error(support_phone)"

#test_naviation_main_pages()
