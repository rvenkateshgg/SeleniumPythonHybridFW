from selenium import webdriver
from selenium.webdriver.common.by import By


class Loginpage():
    textbox_username_Xpath = "//input[@name='user-name']"
    textbox_password_Xpath = "//input[@name='password']"
    btn_Login_Xpath = "//input[@name='login-button']"

    def __init__(self,driver):
        self.driver = driver

    def SetUsername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_Xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_Xpath).send_keys(username)

    def SetPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_Xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_Xpath).send_keys(password)

    def Clickloginbtn(self):
        self.driver.find_element(By.XPATH,self.btn_Login_Xpath).click()



