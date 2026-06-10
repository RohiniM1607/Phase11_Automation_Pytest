from selenium.webdriver.common.by import By

class RegisterPage:

    FirstName = "input-firstname"
    LastName = "input-lastname"
    Email = "input-email"
    Telephone = "input-telephone"
    Password = "input-password"
    ConfirmPassword = "input-confirm"
    Agree = "agree"
    Continue = "//input[@value='Continue']"
    SuccessMessage = "//h1[text()='Your Account Has Been Created!']"
    ErrorMessage = "//div[@class='alert alert-danger alert-dismissible']"

    def __init__(self, driver):
        self.driver = driver

    def enter_details(self, firstname, lastname, email, telephone, password, confirmpassword):
        self.driver.find_element(By.ID, self.FirstName).send_keys(firstname)
        self.driver.find_element(By.ID, self.LastName).send_keys(lastname)
        self.driver.find_element(By.ID, self.Email).send_keys(email)
        self.driver.find_element(By.ID, self.Telephone).send_keys(telephone)
        self.driver.find_element(By.ID, self.Password).send_keys(password)
        self.driver.find_element(By.ID, self.ConfirmPassword).send_keys(confirmpassword)
        self.driver.find_element(By.NAME, self.Agree).click()
        self.driver.find_element(By.XPATH, self.Continue).click()

    def get_success_message(self):
        return self.driver.find_element(By.XPATH, self.SuccessMessage).text

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, self.ErrorMessage).text