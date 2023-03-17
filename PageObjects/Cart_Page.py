from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self,driver):
        self.driver=driver

    cart=(By.XPATH,'//*[@id="shopping_cart_container"]/a')
    Bckpck = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    light = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    shirt = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    fleece = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    Onesie = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
    tshirt = (By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')



    def Cart(self):
        self.driver.find_element(*CartPage.cart).click()

    def Backpack(self):
        self.driver.find_element(*CartPage.Bckpck).click()

    def BikeLight(self):
        self.driver.find_element(*CartPage.light).click()

    def TShirt(self):
        self.driver.find_element(*CartPage.shirt).click()

    def FleeceJacket(self):
        self.driver.find_element(*CartPage.fleece).click()

    def LOnesie(self):
        self.driver.find_element(*CartPage.Onesie).click()

    def RTshirt(self):
        self.driver.find_element(*CartPage.tshirt).click()