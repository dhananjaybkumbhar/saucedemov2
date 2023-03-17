from selenium.webdriver.common.by import By


class CheckoutPage:


    def __init__(self,driver):
        self.driver=driver
    ChkoutBtn = (By.XPATH,'//*[@id="checkout"]')
    fname=(By.XPATH,'//*[@id="first-name"]')
    lname=(By.XPATH,'//*[@id="last-name"]')
    zipc= (By.XPATH,'//*[@id="postal-code"]')
    cbtn=(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[2]/input')


    def CheckoutBtn(self):
        self.driver.find_element(*CheckoutPage.ChkoutBtn).click()

    def FirstName(self,firstname):
        self.driver.find_element(*CheckoutPage.fname).send_keys(firstname)

    def LastName(self,lastname):
        self.driver.find_element(*CheckoutPage.lname).send_keys(lastname)

    def PostalCode(self,postalcode):
        self.driver.find_element(*CheckoutPage.zipc).send_keys(postalcode)

    def ContinueBtn(self):
        self.driver.find_element(*CheckoutPage.cbtn).click()







