from selenium import webdriver
from selenium.webdriver.common.by import By

class CompletePage():
    link_menu_Xpath = "//button[text()='Open Menu']"
    link_logout_Xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def Clickmenubtn(self):
        self.driver.find_element(By.XPATH,self.link_menu_Xpath).click()

    def Clicklogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_Xpath).click()

