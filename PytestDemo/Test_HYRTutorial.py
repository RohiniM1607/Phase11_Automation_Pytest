import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_register():
    driver = webdriver.Chrome()
    driver.get("https://www.hyrtutorials.com/")
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//ul[@id='nav1']/child::li[4]").click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='XPath Practice']"))).click()
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Register']")))
    print("Opened")
    driver.quit()