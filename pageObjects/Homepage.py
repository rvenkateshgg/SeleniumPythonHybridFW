from selenium import webdriver
from selenium.webdriver.common.by import By

class Homepage():
    btn_filter_Xpath = "//select[@class='product_sort_container']"
    btn_value_Xpath = "//option[text()='Price (low to high)']"
    btn_Add_Xpath = "(//button[text()='Add to cart'])[4]"
    link_cart_Xpath = "//a[@class='shopping_cart_link']/span"

    def __init__(self,driver):
        self.driver = driver

    def searchfilter(self):
        self.driver.find_element(By.XPATH,self.btn_filter_Xpath).click()

    def Clickvalue(self):
        self.driver.find_element(By.XPATH,self.btn_value_Xpath).click()

    def addproduct(self):
        self.driver.find_element(By.XPATH,self.btn_Add_Xpath).click()

    def clickcart(self):
        self.driver.find_element(By.XPATH,self.link_cart_Xpath).click()

