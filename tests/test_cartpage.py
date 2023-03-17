from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.Cart_Page import CartPage
from PageObjects.Login_Page import LoginPage

driver=webdriver.Chrome()

driver.get('https://www.saucedemo.com/')

def test_S_Cart_01():
    cart_page=CartPage(driver)
    login_page=LoginPage(driver)
    login_page.userName('standard_user')
    login_page.passWord('secret_sauce')
    login_page.LoginBTN()
    driver.implicitly_wait(7)
    assert driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').is_enabled()

def test_S_Cart_02():
    driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
    assert driver.current_url=='https://www.saucedemo.com/cart.html'
    driver.back()

def test_S_Cart_03():
    driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    assert driver.find_element(By.CSS_SELECTOR,'#shopping_cart_container > a > span').text=='1'

def test_S_Cart_04():
    driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button').click()
    assert driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a > span').text == '2'

def test_S_Cart_05():
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button').click()
    assert driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a > span').text == '3'

def test_S_Cart_06():
    driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    assert driver.switch_to.alert.accept()

def test_S_Cart_07():
    assert driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]').text==driver.find_element(By.CSS_SELECTOR,'#item_4_title_link > div').text

def test_S_Cart_09():
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    assert driver.find_element(By.CSS_SELECTOR,'div.page_wrapper div.cart_contents_container div:nth-child(1) div.cart_list div.cart_item > div.cart_quantity').is_displayed()

def test_S_Cart_10():
    assert driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']").is_enabled()

def test_S_Cart_11():
    driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()
    assert driver.switch_to.alert.accept()


def test_S_Cart_12():
    item_count=driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').text
    if item_count == '2':
        assert driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').is_displayed()


def test_S_Cart_15():
    driver.find_element(By.XPATH,'//*[@id="checkout"]').click()
    assert driver.current_url=='https://www.saucedemo.com/checkout-step-one.html'
    driver.back()

def test_S_Cart_16():
    driver.find_element(By.XPATH,'//*[@id="continue-shopping"]').click()
    assert driver.current_url=='https://www.saucedemo.com/inventory.html'







































