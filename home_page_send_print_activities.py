from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_send_print_activities_home_page():
    try:
        browser = webdriver.Chrome()
        browser.get("https://lb11.mojosells.com/login/")
        browser.implicitly_wait(10)

        #login
        email_input = browser.find_element(By.XPATH, '//input[@name="email"]')
        email_input.clear()
        email_input.send_keys("g.torosyan@g-sg.net")

        password_input = browser.find_element(By.XPATH, '//input[@name="password"]')
        password_input.clear()
        password_input.send_keys("password1")

        browser.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(10)

        #SEND ACTIVITIES TO EMAIL
        browser.find_element(By.CSS_SELECTOR, "button.HomeView_btnEmail__ePnDG").click()
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
        time.sleep(2)
        #Assert activities email sent
        activities_email_info_popup = browser.find_element(By.CSS_SELECTOR, "div.GenericModal_contentContainer__2PwLa")
        time.sleep(2)
        assert activities_email_info_popup.text in "Activities were successfully sent to your email.", \
            "Activities email has not been sent from home page"
        #close Activities were successfully sent popup
        browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_cancelButton__3Scfe").click()

        #PRINT ACTIVITIES
        browser.find_element(By.CSS_SELECTOR, "button.HomeView_btnPrint__2jCZV").click()
        browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
        time.sleep(3)
        #confirm = browser.switch_to.alert
        #confirm.dismiss()

    finally:
        time.sleep(2)
        browser.quit()

test_send_print_activities_home_page()