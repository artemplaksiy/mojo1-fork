from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_navigation_settings(browser):

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

    # go to settings
    browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_hoverContainer__RR9Zd").click()
    browser.find_element(By.CSS_SELECTOR, "div.AccountMenu_menuContainer__2umWR>:nth-child(3)").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.Table_table__2OuB7")))
    # Dialer.Assert Caller ID / Mojo Voice
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Caller ID / Mojo Voice", "No title " \
                                                                                                  "Caller ID / Mojo Voice"
    assert browser.find_element(By.CSS_SELECTOR, "tbody.Table_tbody__38AYG"), "No CallerIDs table"

    dialer_settings_buttons = browser.find_elements(By.CSS_SELECTOR,
                                                    "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")
    # Dialer.Callback message
    dialer_settings_buttons[1].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.SelectField_selectFieldContainer__2R3j0"), "Callback message page error"
    # Dialer.Drop voicemail
    dialer_settings_buttons[2].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.SelectField_selectFieldContainer__2R3j0"), "Drop voicemail page error"
    # Dialer.Dialer Settings
    dialer_settings_buttons[3].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Dialer Settings", "Dialer Settings page error"

    settings_buttons = browser.find_elements(By.CSS_SELECTOR,
                                             "button.SettingsSidebar_link__1MIXW.SettingsSidebar_primaryLink__2HcEp")
    print(settings_buttons)

    # Emails
    # Emails.Email templates
    settings_buttons[1].click()
    assert browser.find_element(By.CSS_SELECTOR, "table.Table_table__2OuB7"), "Emails templates page error"

    emails_settings_buttons = browser.find_elements(By.CSS_SELECTOR,
                                                    "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")
    # Emails.SMTP Settings
    emails_settings_buttons[1].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.SMTPView_info__3SNHp"), "SMTP Settings page error(description)"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "SMTP Settings", "SMTP Settings page error(title)"
    # Emails.Notification
    emails_settings_buttons[2].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Notifications", \
        "Notifications page error(title)"

    # Emails.General
    emails_settings_buttons[3].click()
    assert "If you’re sending your emails across time zones" \
           in browser.find_element(By.CSS_SELECTOR,
                                   "div.GeneralView_desc__16gpP").text, "Email.General page error(description)"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Email Schedule", "Email.General page error(title)"
    # Emails.Google API
    emails_settings_buttons[4].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Gmail", "Email.Gmail page error(title)"

    # Letter
    settings_buttons[2].click()
    assert browser.find_element(By.CSS_SELECTOR, "table.Table_table__2OuB7"), "Letters. Tamplates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Letter Templates", "Letters. Title page error"

    # Action Plan
    settings_buttons[3].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Action plans. Tamplates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Action Plans", "Action plans. Title page error"

    # Scripts/Forms
    settings_buttons[4].click()
    # Scripts/Forms.Lead Sheet
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.LeadSheetView_tableContainer__1kJNU"), "Scripts/Forms.Lead Sheet templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Lead Sheet", "Scripts/Forms.Lead Sheet title page error"
    scripts_buttons = browser.find_elements(By.CSS_SELECTOR,
                                            "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")

    # Scripts/Forms.Lead Sheet
    scripts_buttons[1].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Scripts/Forms.Callins scripts templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Calling Scripts", "Scripts/Forms.Callins scripts title page error"

    # Scripts/Forms.Lead Capture Forms
    scripts_buttons[2].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Scripts/Forms.LeadCaptureForms templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Lead Capture Forms", \
        "Scripts/Forms.LeadCaptureForms title page error"

    # Scripts/Forms.Checklists
    scripts_buttons[3].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Scripts/Forms.Checklists templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Checklists", \
        "Scripts/Forms.Checklists title page error"

    # Data Management
    settings_buttons[5].click()
    # Data Management.Misc Fields
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Misc Fields templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Misc Fields", \
        "Data Management.Misc Fields title page error"

    data_managment_buttons = browser.find_elements(By.CSS_SELECTOR,
                                                   "button.SettingsSidebar_link__1MIXW.SettingsSidebar_secondaryLink__3SjP0")

    # Data Management.Import history
    data_managment_buttons[1].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Import history templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Import History", \
        "Data Management.Import history title page error"

    # Data Management.Restore Deleted Data
    data_managment_buttons[2].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Restore Deleted Data templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Restore Deleted Data", \
        "Data Management.Restore Deleted Data title page error"

    # Data Management.Export history
    data_managment_buttons[3].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Export history templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Export History", \
        "Data Management.Export history title page error"

    # Data Management.DNC Scrubbing
    data_managment_buttons[4].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.DNC Scrubbing templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "DNC Scrubbing", \
        "Data Management.DNC Scrubbing title page error"

    # Data Management.DNC Export
    data_managment_buttons[5].click()
    assert "You can submit a request" in browser.find_element(By.CSS_SELECTOR,
                                                              "div.Generic_text1__2k4Cx").text, "Data Management.DNC Export description page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "DNC Export", \
        "Data Management.DNC Export title page error"

    # Data Management.DNC History
    data_managment_buttons[6].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.DNC History templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "DNC History", \
        "Data Management.DNC History title page error"

    # Data Management.Contact Source
    data_managment_buttons[7].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "table.Table_table__2OuB7"), "Data Management.Contact Source templates table page error"
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Contact Source", \
        "Data Management.Contact Source title page error"

    # Data Management.Appearance
    settings_buttons[6].click()
    assert browser.find_element(By.CSS_SELECTOR,
                                "div.Generic_subtitle2__3FiOt").text in "Appearance", \
        "Data Management.Appearance title page error"

#test_navigation_settings()
