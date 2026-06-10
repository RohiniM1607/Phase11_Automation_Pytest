import pytest
import time
from selenium.webdriver.common.by import By
from Utilities import ExcelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import LogCreator


@pytest.mark.parametrize("firstname, lastname, email, telephone, password, confirmpassword", ExcelReader.get_data("ExcelFiles/TestData.xlsx", "Register"))
@pytest.mark.usefixtures("setup_and_teardown")
class Test_Register:
    def test_register(self, firstname, lastname, email, telephone, password, confirmpassword):
        logger = LogCreator.log_generator()
        logger.info("Register User Account")
        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        logger.info("Entering firstname")
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstname)
        logger.info("Entering last")
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastname)
        logger.info("Entering email:")
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        logger.info("Entering telephone")
        self.driver.find_element(By.ID, "input-telephone").send_keys(telephone)
        logger.info("Entering password")
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        logger.info("Entering confirm password")
        self.driver.find_element(By.ID, "input-confirm").send_keys(confirmpassword)
        self.driver.find_element(By.NAME, "agree").click()
        logger.info("Accepting terms and conditions")
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        logger.info("Clicking on continue button")

        try:
            success_msg = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Your Account Has Been Created!']")))

            assert success_msg.text == "Your Account Has Been Created!"
            print("Registration successful.")
            logger.info("User account registeration successfully")

        except:
            error_msg = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")))

            assert error_msg.is_displayed()
            print("Registration failed:", error_msg.text)
            logger.info("User account registeration failed")
