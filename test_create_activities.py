from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def test_create_activities_from_cs():
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
        # Assert Home Page
        join_webinar_button = browser.find_element(By.CSS_SELECTOR, "div.HomeView_textContent__2L3mx")
        assert join_webinar_button.text in "Join Webinar", "something wrong with home page"

        #APP CREATION
        #Go to DataDialer
        browser.find_element(By.XPATH, '//button[@class="MainMenuButton_button__Wxat6 "]/img[@alt="Data & Dialer"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Table_tableFixed__3MyJT")))
        #Assert DataDialer page
        header_data_dialer = browser.find_element(By.CSS_SELECTOR, "div.Generic_subtitle2__3FiOt")
        assert header_data_dialer.text in "All Contacts", "Error DataDialer page load"

        #Search
        global_search_field = browser.find_element(By.CSS_SELECTOR, "button.DummySidebarSearch_searchInputContainer__46fue")
        global_search_field.click()
        #time.sleep(4)
        browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__33nNB").send_keys("Knoxville2711")
        #time.sleep(4)
        #wait(EC.presence_of_element_located((By.CSS_SELECTOR, "button.styles_btn__1cyQv")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ContactGroup_arrow__tSmCX")))
        browser.find_element(By.CSS_SELECTOR, "div.ContactGroup_arrow__tSmCX").click()
        browser.find_element(By.CSS_SELECTOR, "div.SearchResults_resultField__1Mqdp.SearchResults_resultItemFullName__21KTL").click()

        # create app
        browser.find_element   (By.XPATH, '//img[@src="/static/media/add-appt-icon.3aeee97e.svg"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.GenericModal_title__34niQ")))
        # input title, description
        browser.find_element(By.CSS_SELECTOR, "input.AppointmentPopup_textInput__3Q_R4").send_keys("app title autotest")
        browser.find_element(By.CSS_SELECTOR, "textarea.AppointmentPopup_descriptionTextarea__1zZTz").send_keys("app description autotest")
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_mainContainer__ecgLX")))
        # click on Activities section in CS
        browser.find_element(By.CSS_SELECTOR, "#contactPopover div.SidebarLink_link__3AKAg#activities").click()
        assert browser.find_element(By.CSS_SELECTOR, "span.ContactActivity_title__1LxXW").text in "app title autotest", \
            "app was not created"

        #go to Calendar
        browser.find_element(By.XPATH, '//img[@src="/static/media/menu-calendar.a14c050d.svg"]').click()
        browser.find_element(By.CSS_SELECTOR, "button.confirmAlert_actionButton__nRyS0.confirmAlert_actionButtonConfirm__2nOW7").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Table_tableFixed__3MyJT")))

        #search Knoxville2711 app event
        calendar_search = browser.find_element(By.CSS_SELECTOR, "input.CalendarTableView_searchInput__18SdX")
        calendar_search.clear()
        calendar_search.send_keys("Knoxville2711")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.Table_tr__1tLPZ.Table_trClickable__1UdAH")))
        #delete Knoxville2711 app event
        browser.find_element(By.CSS_SELECTOR, "button.ContextMenu_contextButton__3LrLO").click()
        browser.find_elements(By.CSS_SELECTOR, "button.PopoverMenu_menuButton__2MQjV")[2].click()
        browser.find_element(By.CSS_SELECTOR, "button.confirmAlert_actionButton__nRyS0.confirmAlert_actionButtonConfirm__2nOW7").click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "tr.Table_tr__1tLPZ.Table_trClickable__1UdAH")))


        #TASK CREATION
        # Go to DataDialer
        browser.find_element(By.XPATH,
                             '//button[@class="MainMenuButton_button__Wxat6 "]/img[@alt="Data & Dialer"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Table_tableFixed__3MyJT")))
        # Assert DataDialer page
        header_data_dialer = browser.find_element(By.CSS_SELECTOR, "div.Generic_subtitle2__3FiOt")
        assert header_data_dialer.text in "All Contacts", "Error DataDialer page load"

        # Search
        global_search_field = browser.find_element(By.CSS_SELECTOR,
                                                   "button.DummySidebarSearch_searchInputContainer__46fue")
        global_search_field.click()
        browser.find_element(By.XPATH, '//img[@src="/static/media/search-clear-icon.dee7a556.svg"]').click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.ContactGroup_arrow__tSmCX")))
        browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__33nNB").send_keys("Knoxville2711")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ContactGroup_arrow__tSmCX")))
        browser.find_element(By.CSS_SELECTOR, "div.ContactGroup_arrow__tSmCX").click()
        browser.find_element(By.CSS_SELECTOR,
                             "div.SearchResults_resultField__1Mqdp.SearchResults_resultItemFullName__21KTL").click()

        # create task
        browser.find_element(By.XPATH, '//img[@src="/static/media/add-task-icon.816cf495.svg"]').click()
        browser.find_element(By.CSS_SELECTOR, "input.TaskPopup_textInput__2wRI9").send_keys("task title autotest")
        browser.find_element(By.CSS_SELECTOR, "textarea.TaskPopup_descriptionTextarea__28A6J").send_keys("task description autotest")
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_mainContainer__ecgLX")))
        # click on Activities section in CS
        browser.find_element(By.CSS_SELECTOR, "#contactPopover div.SidebarLink_link__3AKAg#activities").click()
        assert browser.find_element(By.CSS_SELECTOR, "span.ContactActivity_title__1LxXW").text in "task title autotest", \
            "task was not created"

        # go to Calendar
        browser.find_element(By.XPATH, '//img[@src="/static/media/menu-calendar.a14c050d.svg"]').click()
        browser.find_element(By.CSS_SELECTOR,
                             "button.confirmAlert_actionButton__nRyS0.confirmAlert_actionButtonConfirm__2nOW7").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Table_tableFixed__3MyJT")))

        # search Knoxville2711 task event
        calendar_search = browser.find_element(By.CSS_SELECTOR, "input.CalendarTableView_searchInput__18SdX")
        calendar_search.clear()
        calendar_search.send_keys("Knoxville2711")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.Table_tr__1tLPZ.Table_trClickable__1UdAH")))
        # delete Knoxville2711 app event
        browser.find_element(By.CSS_SELECTOR, "button.ContextMenu_contextButton__3LrLO").click()
        browser.find_elements(By.CSS_SELECTOR, "button.PopoverMenu_menuButton__2MQjV")[2].click()
        browser.find_element(By.CSS_SELECTOR,
                             "button.confirmAlert_actionButton__nRyS0.confirmAlert_actionButtonConfirm__2nOW7").click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "tr.Table_tr__1tLPZ.Table_trClickable__1UdAH")))

        #FU Call creation
        # Go to DataDialer
        browser.find_element(By.XPATH,
                             '//button[@class="MainMenuButton_button__Wxat6 "]/img[@alt="Data & Dialer"]').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Table_tableFixed__3MyJT")))
        # Assert DataDialer page
        header_data_dialer = browser.find_element(By.CSS_SELECTOR, "div.Generic_subtitle2__3FiOt")
        assert header_data_dialer.text in "All Contacts", "Error DataDialer page load"

        # Search
        global_search_field = browser.find_element(By.CSS_SELECTOR,
                                                   "button.DummySidebarSearch_searchInputContainer__46fue")
        global_search_field.click()
        browser.find_element(By.XPATH, '//img[@src="/static/media/search-clear-icon.dee7a556.svg"]').click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.ContactGroup_arrow__tSmCX")))
        browser.find_element(By.CSS_SELECTOR, "input.SidebarSearch_searchInput__33nNB").send_keys("Knoxville2711")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ContactGroup_arrow__tSmCX")))
        browser.find_element(By.CSS_SELECTOR, "div.ContactGroup_arrow__tSmCX").click()
        browser.find_element(By.CSS_SELECTOR,
                             "div.SearchResults_resultField__1Mqdp.SearchResults_resultItemFullName__21KTL").click()

        # fu call creation
        browser.find_element(By.XPATH, '//img[@src="/static/media/add-f_call-icon.b35c81a6.svg"]').click()
        browser.find_element(By.CSS_SELECTOR, "input.FollowUpCallPopup_textInput__2BYvH").send_keys("fu call title autotest")
        browser.find_element(By.CSS_SELECTOR, "textarea.FollowUpCallPopup_descriptionTextarea__3tsG1").send_keys("fu call description autotest")
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, "button.GenericModal_button__1wlPS.GenericModal_confirmButton__1VoK5").click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.GenericModal_mainContainer__ecgLX")))
        # click on Activities section in CS
        browser.find_element(By.CSS_SELECTOR, "#contactPopover div.SidebarLink_link__3AKAg#activities").click()
        assert browser.find_element(By.CSS_SELECTOR, "span.ContactActivity_title__1LxXW").text in "fu call title autotest", \
            "task was not created"

        # go to Calendar
        browser.find_element(By.XPATH, '//img[@src="/static/media/menu-calendar.a14c050d.svg"]').click()
        browser.find_element(By.CSS_SELECTOR,
                             "button.confirmAlert_actionButton__nRyS0.confirmAlert_actionButtonConfirm__2nOW7").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Table_tableFixed__3MyJT")))

        # search Knoxville2711 FU call event
        calendar_search = browser.find_element(By.CSS_SELECTOR, "input.CalendarTableView_searchInput__18SdX")
        calendar_search.clear()
        calendar_search.send_keys("Knoxville2711")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.Table_tr__1tLPZ.Table_trClickable__1UdAH")))
        # delete Knoxville2711 FU call event
        browser.find_element(By.CSS_SELECTOR, "button.ContextMenu_contextButton__3LrLO").click()
        browser.find_elements(By.CSS_SELECTOR, "button.PopoverMenu_menuButton__2MQjV")[2].click()
        browser.find_element(By.CSS_SELECTOR,
                             "button.confirmAlert_actionButton__nRyS0.confirmAlert_actionButtonConfirm__2nOW7").click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, "tr.Table_tr__1tLPZ.Table_trClickable__1UdAH")))

        # Logout
        browser.find_element(By.CSS_SELECTOR, "div.Placeholder_caption__O4F-Z").click()
        browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_link__2RBsi").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")))
        # Assert login page
        login_page_header = browser.find_element(By.CSS_SELECTOR, "div.SignInData_Title__2zl3Q")
        assert login_page_header.text in "Sign In to Mojo", "Login page Error(header)"
        support_phone = browser.find_element(By.CSS_SELECTOR, "span.CallTollFree_CallTollFreePhone__3vqFR")
        assert support_phone.text in "877-859-6656", "Login page Error(support_phone)"


    finally:
        browser.quit()
test_create_activities_from_cs()