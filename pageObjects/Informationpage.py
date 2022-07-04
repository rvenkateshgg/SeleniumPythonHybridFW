from selenium import webdriver
from selenium.webdriver.common.by import By


class Informationpage():
    textbox_fname_Xpath = "//input[@id='first-name']"
    textbox_lname_Xpath = "//input[@id='last-name']"
    textbox_zipcode_Xpath = "//input[@id='postal-code']"
    btn_continue_Xpath = "//input[@id='continue']"

    def __init__(self,driver):
        self.driver = driver

    def SetFname(self,fname):
        self.driver.find_element(By.XPATH,self.textbox_fname_Xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_fname_Xpath).send_keys(fname)

    def SetLname(self,lname):
        self.driver.find_element(By.XPATH,self.textbox_lname_Xpath)
        self.driver.find_element(By.XPATH,self.textbox_lname_Xpath).send_keys(lname)

    def SetZcode(self,zipcode):
        self.driver.find_element(By.XPATH,self.textbox_zipcode_Xpath)
        self.driver.find_element(By.XPATH,self.textbox_zipcode_Xpath).send_keys(zipcode)

    def ClickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_continue_Xpath).click()

