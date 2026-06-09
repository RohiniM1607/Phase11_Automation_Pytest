import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Utilities.logCreator import log_generator

@pytest.mark.parametrize("username, password", excelReader.get_data("ExcelFiles/LoginData.xlsx", "Login"))
class TestLogin1:
    def test_validlogin1(self, username, password):
        logger = log_generator()
        self.driver = webdriver.Chrome()
        logger.info("Opening Chrome Browser")
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        logger.info("Launching Demoblaze Application")
        self.driver.find_element(By.ID, "login2").click()
        time.sleep(2)
        logger.info("Entering the login credentials")
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()= 'Log in']").click()
        logger.info("Closing web browser")
        logger.info("-------------------------------------")
        self.driver.quit()