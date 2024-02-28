from behave import *

from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

use_step_matcher('parse')

browser = webdriver.Chrome(service=Service(executable_path=binary_path))
wait = WebDriverWait(browser, 15)
browser.implicitly_wait(15)


@step("browser is opened")
def step_impl(context):
    global browser

    if not browser:
        browser = webdriver.Chrome(service=Service(executable_path=binary_path))
        print("Opening browser...")
    else:
        print("Browser already opened")


@step('I go on page "{page}"')
def step_impl(context, page):
    print("Opening page: ", page)
    browser.get(page)


@step('fill "{email}" in field "Email"')
def step_impl(context, email):
    email_element = browser.find_element(By.XPATH, '//input[@name="email"]')
    email_element.clear()
    email_element.send_keys(email)


@step('fill "{password}" in field "Password"')
def step_impl(context, password):
    password_element = browser.find_element(By.XPATH, '//input[@name="password"]')
    password_element.clear()
    password_element.send_keys(password)


@step('click "Submit"')
def step_impl(context):
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    # TODO: this should not be right here
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.HomeView_newsTitle__VgBZL")))


@step("I should be logged in")
def step_impl(context):
    join_webinar_button = browser.find_element(By.CSS_SELECTOR, "div.HomeView_textContent__2L3mx")
    assert join_webinar_button.text in "Join Webinar", "something wrong with home page"


@step('"Invalid login/password" should be displayed')
def step_impl(context):
    # TODO: avoid any king of dynamic IDs in page
    error_messages = browser.find_elements(By.XPATH, '//*[starts-with(@class, "Form_NonFieldErrors")]')
    if len(error_messages) > 0:
        print("Expected error message was displayed")
    else:
        raise RuntimeError("Expected error message was not displayed!")