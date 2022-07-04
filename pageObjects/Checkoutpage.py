from selenium import webdriver
from selenium.webdriver.common.by import By

class Checkoutpage():
    btn_finish_Xpath = "//button[@id='finish']"

    def __init__(self,driver):
        self.driver = driver

    def ClickFinish(self):
        self.driver.find_element(By.XPATH,self.btn_finish_Xpath).click()