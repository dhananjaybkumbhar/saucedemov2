from selenium.webdriver.common.by import By


class LoginPage:


    def __init__(self,driver):

        self.driver=driver
        # self.wait= driver.implicit_wait(10)
    username_field=(By.ID,'user-name')
    password_field=(By.ID,'password')
    login_btn=(By.ID,'login-button')

    def userName(self,username):
            self.driver.find_element(*LoginPage.username_field).send_keys(username)


    def passWord(self,password):
            self.driver.find_element(*LoginPage.password_field).send_keys(password)


    def LoginBTN(self):
            self.driver.find_element(*LoginPage.login_btn).click()






