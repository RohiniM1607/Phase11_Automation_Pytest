from selenium.webdriver.common.by import By

class HomePage:

    Myaccount = "//a[@title='My Account']"
    Register = "//a[text()='Register']"
    Login = "//a[text()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def click_Register(self):
        self.driver.find_element(By.XPATH, self.Myaccount).click()
        self.driver.find_element(By.XPATH, self.Register).click()

    def click_Login(self):
        self.driver.find_element(By.XPATH, self.Myaccount).click()
        self.driver.find_element(By.XPATH, self.Login).click()
        