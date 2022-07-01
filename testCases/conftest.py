from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='/Users/venkateshr/PycharmProjects/SeleniumProject/drivers/chromedriver')
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=s)
        print("Launching Chrome browser........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='/Users/venkateshr/PycharmProjects/SeleniumProject/drivers/geckodriver')
        print("Launching Firefox browser.......")
    else:
        driver = webdriver.Chrome(service=s)
        print("Launch Chrome browser........")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.addoption("--browser")