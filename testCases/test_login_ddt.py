import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import Xlutils
from selenium.webdriver.chrome.service import Service
import time

s = Service(executable_path="/Users/venkateshr/PycharmProjects/SeleniumPythonHybridFW/drivers/chromedriver")

class Test_WeightGurus():
    path = "/Users/venkateshr/Desktop/datadrivenwglogin.xlsx"

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()
        self.driver.quit()

    def test_signup(self,setup):
        self.driver.get("http://192.168.0.118:8100/landing")
        time.sleep(1)
        self.rows = Xlutils.getRowcount(self.path, 'Sheet1')
        print("No of rows:", self.rows)

        for r in range(2, self.rows + 1):
            self.username = Xlutils.readData(self.path, 'Sheet1', r, 1)
            self.password = Xlutils.readData(self.path, 'Sheet1', r, 2)

            self.driver.find_element(By.XPATH, "(//ion-button[@shape='round'])[1]").click()
            time.sleep(2)

            username1 = self.driver.find_element(By.XPATH, "//ion-input[@type='email']/input")
            username1.clear()
            username1.send_keys(self.username)
            time.sleep(1)
            password1 = self.driver.find_element(By.XPATH, "//input[@name='ion-input-1']")
            password1.clear()
            password1.send_keys(self.password)
            self.driver.find_element(By.XPATH, "//ion-button[@size='large']").click()
            time.sleep(8)

            try:
                self.driver.find_element(By.XPATH, "//ion-label[text()='Body Fat']")
                print("PASS")
                Xlutils.writeData(self.path, 'Sheet1', r, 3, "Test Passed")
            except:
                print("FAIL")
                Xlutils.writeData(self.path, 'Sheet1', r, 3, "Test Failed")
