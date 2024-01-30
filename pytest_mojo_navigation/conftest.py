from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    print("\nbrowser start")
    browser = webdriver.Chrome()
    yield browser
    print("\nbrowser end")
    browser.quit()


