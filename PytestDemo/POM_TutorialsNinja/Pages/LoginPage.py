from selenium.webdriver.common.by import By
from Utilities import Read_config

class LoginPage:
    email = "input-email"
    password = "input-password"
    login_btn = "//input[@value='Login']"
    home_page = "//h2[text()='My Account']"

    def __init__(self, driver):
        self.driver = driver

    def enter_credentials(self, login_email, login_password):
        self.driver.find_element(By.ID, self.email).send_keys(login_email)
        self.driver.find_element(By.ID, self.password).send_keys(login_password)
        self.driver.find_element(By.XPATH, self.login_btn).click()

    def get_homepage_title(self):
        return self.driver.find_element(By.XPATH, self.home_page).text
