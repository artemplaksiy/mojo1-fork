from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def test_import_file_csv():
    try:
        browser = webdriver.Chrome()
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

        #press button import file
        browser.find_element(By.CSS_SELECTOR, "button#import_file").click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//img[@alt="data import video"]')))

        #assert availability Choose file button
        choose_file_button = browser.find_element(By.CSS_SELECTOR, "div.WelcomeView_section__2A-sM>button.Button_btn__1Lkv5")
        assert choose_file_button.text in "Choose File", "There in no Choose file button"

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'scoreboard_good_excel_edited.csv')
        choose_file = browser.find_element(By.CSS_SELECTOR, "input#actual-btn")
        choose_file.send_keys(file_path)

        browser.find_element(By.CSS_SELECTOR, "button.NextButton_button__1oH4w").click()

        #Step 2: Create or Choose an Existing List or Group
        wait.until(EC.presence_of_element_located((By.XPATH, '//img[@alt="Import Step 2"]')))
        #assert lists groups container
        assert browser.find_element(By.CSS_SELECTOR, "div#select_list_or_group_container"), "Something with Step 2 page"
        #creation new list for import
        browser.find_element(By.CSS_SELECTOR, "button#select_field_1_add_btn").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.GenericModal_title__34niQ")))
        browser.find_element(By.CSS_SELECTOR, "input.CreateElementModal_textInput__-5kex").send_keys("0101 auto new1")
        browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_title__34niQ")))
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.NextButton_button__1oH4w")))
        browser.find_element(By.CSS_SELECTOR, "button.NextButton_button__1oH4w").click()


        #Step 3: Map Your Fields
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#fields_mapper_container")))
        #assert step 3
        assert browser.find_elements(By.CSS_SELECTOR, "div.MappingView_stepDescription__2k0Pq"), "Something with Step 3 page"
        duplicates_modes_list = browser.find_elements(By.CSS_SELECTOR, "div.Checkbox_title__1isC4")
        duplicates_modes_list[0].click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, "button.NextButton_button__1oH4w").click()

        #Step 4: Finish Import
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.FinishImportView_videoThumbnail__1WMjp")))
        #assert step 4
        assert browser.find_element(By.CSS_SELECTOR, "div.FinishImportView_mappedFieldsContainer__2TJUr"), "Something with Step 4 page"
        browser.find_element(By.CSS_SELECTOR, "button.FinishImportView_genericButton__3NMuh").click()

        #DataDialer pape
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ContactTable_tableContainer__1FK5t")))
        assert browser.find_element(By.CSS_SELECTOR, "div.Table_bottomActionsAndPaginationContainer__2LZDu"), \
            "Something with Data Dialer page"
        #search imported contact
        browser.find_element(By.CSS_SELECTOR, "div.DummySidebarSearch_searchInput__r-3bx").click()
        browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__33nNB").send_keys("Autotest Knoxville")
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.styles_btn__1cyQv")))
        view_all_results_button = browser.find_element(By.CSS_SELECTOR, "button.styles_btn__1cyQv")

        assert view_all_results_button.text in "View All Results In Table", "there is no imported contact in data"
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, "div.SidebarSearch_closeAnchorArrow__4Gvt6").click()

        #maybe here shoud be some wait
        browser.find_element(By.CSS_SELECTOR, "input.SelectField_searchBarSide__1MlwY").send_keys("0101 auto new1")
        assert browser.find_element(By.CSS_SELECTOR, "div.SelectFieldElement_name__hX6bR").text in \
               "0101 auto new1", "no searched list created during import 0101 auto new1"
        #deleting list created during import 0101 auto new1
        browser.find_element(By.CSS_SELECTOR, "div.SelectFieldElement_manageWrapper__2-hy9").click()
        #time.sleep(2)
        browser.find_elements(By.CSS_SELECTOR, "div.SelectFieldElement_menuItem__3GbRz")[4].click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.GenericModal_title__34niQ")))
        browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR,"div.GenericModal_title__34niQ")))

        # logout
        browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_hoverContainer__RR9Zd").click()
        browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_link__2RBsi").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")))
        # Assert login page
        login_title = browser.find_element(By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")
        assert login_title.text in "Sign In to Mojo", "something with login page"

    finally:
        time.sleep(2)
        browser.quit()

test_import_file_csv()

