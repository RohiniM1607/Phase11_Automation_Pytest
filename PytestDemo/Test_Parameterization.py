import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('search_term', [('Selenium'), ('Pytest'), ('Selenium Locatores')])
def test_google_search(search_term):
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    search_box = driver.find_element(By.XPATH, "//textarea[@class='gLFyf']")
    search_box.send_keys(search_term)
    
