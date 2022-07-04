from selenium import webdriver
from selenium.webdriver.common.by import By

class Cartpage():
    btn_checkout_Xpath = "//button[@id='checkout']"

    def __init__(self,driver):
        self.driver = driver

    def Clickcheckout(self):
        self.driver.find_element(By.XPATH,self.btn_checkout_Xpath).click()

