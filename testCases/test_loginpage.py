import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.Loginpage import Loginpage
from pageObjects.Homepage import Homepage
from pageObjects.Cartpage import Cartpage
from pageObjects.Informationpage import Informationpage
from pageObjects.Checkoutpage import Checkoutpage
from pageObjects.Completepage import CompletePage

class Test_001_Saucelab():
    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    def test_HomePagetitle(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Swags Labs":
            assert True
        else:
            assert False

    def test_Loginpage(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(2)
        self.lp = Loginpage(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.SetPassword(self.password)
        self.lp.Clickloginbtn()
        time.sleep(2)

        self.hp = Homepage(self.driver)
        self.hp.searchfilter()
        self.hp.Clickvalue()
        self.hp.addproduct()
        self.hp.clickcart()
        time.sleep(2)

        self.cp = Cartpage(self.driver)
        self.cp.Clickcheckout()
        time.sleep(2)

        self.ip = Informationpage(self.driver)
        self.ip.SetFname("Venkatesh")
        self.ip.SetLname("R")
        self.ip.SetZcode("600077")
        self.ip.ClickContinue()
        time.sleep(2)

        self.ch = Checkoutpage(self.driver)
        self.ch.ClickFinish()
        time.sleep(2)

        self.co = CompletePage(self.driver)
        self.co.Clickmenubtn()
        time.sleep(1)
        self.co.Clicklogout()
        time.sleep(3)
        print("Pass")




