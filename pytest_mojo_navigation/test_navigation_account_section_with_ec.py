from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_navigation_account_with_ec(browser):

    browser.get("https://lb11.mojosells.com/login/")
    wait = WebDriverWait(browser, 10)
    browser.implicitly_wait(10)

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

    # Account_profile
    #wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.AccountMenu_hoverContainer__RR9Zd"))).click()
    #wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="AccountMenu_menuContainer__2umWR"]/a[@href="/account/profile/"]'))).click()
    browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_hoverContainer__RR9Zd").click()
    browser.find_element(By.XPATH, '//div[@class="AccountMenu_menuContainer__2umWR"]/a[@href="/account/profile/"]').click()
    # Assert Profile page
    contact_info_title = browser.find_element(By.CSS_SELECTOR, "div.Generic_subtitle2__3FiOt")
    assert contact_info_title.text in "Contact Information", "something with Account-Profile page"

    # Billing
    browser.find_element(By.XPATH, '//a[@href="/account/billing/"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.Generic_subtitle__vnJT2")))
    # Assert Billing page
    billing_titile = browser.find_element(By.CSS_SELECTOR, "div.Generic_subtitle2__3FiOt")
    assert billing_titile.text in "Billing", "something with Billing page"

    # Agents
    browser.find_element(By.XPATH, '//a[@href="/account/agents/"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.AccountAgentsView_userTypesLink__3Uu1r")))
    # Assert Agents page
    agent_info_description = browser.find_element(By.CSS_SELECTOR, "div.AccountAgentsView_notice__3CYzz")
    assert "Deleting agents can be" in agent_info_description.text, "something with Agent Information page"

    # Subscriptions
    browser.find_element(By.XPATH, '//a[@href="/account/subscriptions/"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.AccountSubscriptionsView_title__3oVLs")))
    # Assert Subscription page
    subscriprion_desc = browser.find_element(By.CSS_SELECTOR, "div.AccountSubscriptionsView_subtitle__3fIMk")
    assert "Below is your current subscription" in subscriprion_desc.text, "something with Subscription page"

    # Refer a Friend Invites
    browser.find_element(By.XPATH, '//a[@href="/account/refer-friend/"]').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.Generic_subtitle2__3FiOt")))
    # Assert Refer a Friend
    refer_friend_desc = browser.find_element(By.CSS_SELECTOR, "div.Generic_text1__2k4Cx")
    assert "Referral invites stay active" in refer_friend_desc.text, "something with Refer A Friend page"


#test_navigation_account_with_ec()