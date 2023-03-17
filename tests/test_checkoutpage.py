import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Cart_Page import CartPage
from PageObjects.Checkout_Page import CheckoutPage
from PageObjects.Login_Page import LoginPage

driver=webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

def test_S_Checkout_01():
    check_out_page=CheckoutPage(driver)
    login_page = LoginPage(driver)
    cart_page=CartPage(driver)
    login_page.userName('standard_user')
    login_page.passWord('secret_sauce')
    login_page.LoginBTN()
    cart_page.BikeLight()
    cart_page.Backpack()
    cart_page.Cart()
    check_out_page.CheckoutBtn()
    assert driver.current_url=='https://www.saucedemo.com/checkout-step-one.html'
    time.sleep(2)
    # driver.back()

# def test_S_Checkout_02():

def test_S_Checkout_03():
    assert driver.find_element(By.XPATH,'//*[@id="first-name"]').is_displayed()
    assert driver.find_element(By.XPATH,'//*[@id="last-name"]').is_displayed()
    assert driver.find_element(By.XPATH,'//*[@id="postal-code"]').is_displayed()
    assert driver.find_element(By.XPATH,'//*[@id="address"]').is_displayed()

def test_S_Checkout_04():
    check_out_page = CheckoutPage(driver)
    check_out_page.FirstName('Dhananjay')
    check_out_page.LastName('K')
    check_out_page.PostalCode('1230')
    assert driver.find_element(By.XPATH,'//*[@id="first-name"]').get_attribute('value')=='Dhananjay'
    assert driver.find_element(By.XPATH,'//*[@id="last-name"]').get_attribute('value')=='K'
    assert driver.find_element(By.XPATH,'//*[@id="postal-code"]').get_attribute('value')=='1230'
    driver.back()

def test_S_Checkout_05():
    check_out_page = CheckoutPage(driver)
    check_out_page.CheckoutBtn()
    check_out_page.FirstName('')
    check_out_page.LastName('')
    check_out_page.PostalCode('')
    check_out_page.ContinueBtn()
    msg=driver.find_element(By.CSS_SELECTOR,'#checkout_info_container > div > form > div.checkout_info > div.error-message-container.error').text
    assert msg=='Error: First Name is required'
    driver.get_screenshot_as_file('test5.png')

def test_S_Checkout_06():
    check_out_page = CheckoutPage(driver)
    check_out_page.FirstName('Dhananjay')
    check_out_page.LastName('')
    check_out_page.PostalCode('')
    check_out_page.ContinueBtn()
    msg = driver.find_element(By.CSS_SELECTOR,'#checkout_info_container > div > form > div.checkout_info > div.error-message-container.error').text
    assert msg == 'Error: Last Name is required'
    driver.back()

def test_S_Checkout_07():
    check_out_page = CheckoutPage(driver)
    check_out_page.CheckoutBtn()
    check_out_page.FirstName('Dhananjay')
    check_out_page.LastName('K')
    check_out_page.PostalCode('')
    check_out_page.ContinueBtn()
    msg = driver.find_element(By.CSS_SELECTOR,'#checkout_info_container > div > form > div.checkout_info > div.error-message-container.error').text
    assert msg == 'Error: Postal Code is required'
    driver.back()


def test_S_Checkout_08():
    check_out_page = CheckoutPage(driver)
    check_out_page.CheckoutBtn()
    check_out_page.FirstName('Dhananjay')
    check_out_page.LastName('K')
    check_out_page.PostalCode('1230')
    check_out_page.ContinueBtn()
    assert driver.current_url=='https://www.saucedemo.com/checkout-step-two.html'

def test_S_Checkout_12():
    assert driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[1]').is_selected()

def test_S_Checkout_10():
    btn= driver.find_element(By.XPATH,'//*[@id="cancel"]').click()
    assert driver.current_url=='https://www.saucedemo.com/inventory.html'

def test_S_Checkout_11():
    driver.find_element(By.XPATH,'//*[@id="finish"]').click()
    msg= driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]').get_attribute('complete-header')
    assert msg=='THANK YOU FOR YOUR ORDER'



























































