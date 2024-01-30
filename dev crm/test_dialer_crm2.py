from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_new_dialer():
    try:
        browser = webdriver.Chrome()
        browser.get("https://devlb.mojosells.com/crm/login/")
        wait = WebDriverWait(browser, 15)
        browser.implicitly_wait(20)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#submit")))
        #login into crm
        browser.find_element(By.CSS_SELECTOR, "input#id_username").clear()
        browser.find_element(By.CSS_SELECTOR, "input#id_username").send_keys("gabik")
        browser.find_element(By.CSS_SELECTOR, "input#id_password").clear()
        browser.find_element(By.CSS_SELECTOR, "input#id_password").send_keys("123gabik00t0r")
        browser.find_element(By.CSS_SELECTOR, "input#submit").click()
        browser.get("https://devlb.mojosells.com/crm/dialers_status/")

        #press test1
        browser.find_element(By.XPATH, '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test2
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test3
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test4
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test5
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test6
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test7
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test8
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test9
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test10
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test1
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test2
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test3
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test4
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test5
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test6
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test7
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test8
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test9
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()

        # press test10
        browser.find_element(By.XPATH,
                             '//button[@onclick="event.stopPropagation(); testServerPopup([{name: \'M4\', host: \'192.168.50.102\'}]);"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_proxy_buttonContinue").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button#jqi_report_buttonClose")))
        browser.find_element(By.CSS_SELECTOR, "button#jqi_report_buttonClose").click()


        #time.sleep(3)

    finally:
        #time.sleep(3)
        browser.quit()

#test_new_dialer()
