import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Login_Page import  LoginPage
from utilities.BaseClass import Baseclass

driver=webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

class TestLoginPage(Baseclass):


    def test_S_Login_01(self):
        driver.get('https://www.saucedemo.com/')
        login_page=LoginPage(driver)
        assert driver.find_element(By.ID,'user-name').is_enabled()
        assert driver.find_element(By.ID,'password').is_enabled()

    def test_S_Login_02(self):
        login_page=LoginPage(driver)
        assert driver.find_element(By.ID,'login-button').is_enabled()


    def test_S_Login_03_04_05 (self, getTestData):
        log=self.getLogger()
        login_page=LoginPage(self.driver)
        log.info('username is'+getTestData['username'])
        login_page.userName(getTestData['username'])
        login_page.passWord(getTestData['password'])
        login_page.LoginBTN()
        driver.implicitly_wait(10)
        assert driver.current_url=='https://www.saucedemo.com/inventory.html'
        time.sleep(3)
        driver.back()


    def test_S_Login_07():
        login_page=LoginPage(driver)
        login_page.LoginBTN()
        msg = driver.find_element(By.CSS_SELECTOR,'#login_button_container > div > form > div.error-message-container.error').text
        assert msg=='Epic sadface: Username is required'

    def test_S_Login_08():
        login_page = LoginPage(driver)
        login_page.userName(' ')
        login_page.passWord(' ')
        login_page.LoginBTN()
        msg = driver.find_element(By.CSS_SELECTOR,'#login_button_container > div > form > div.error-message-container.error').text
        assert msg=='Epic sadface: Username and password do not match any user in this service'

















