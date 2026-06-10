import pytest
from selenium import webdriver

@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    

    driver.maximize_window()
    driver.implicitly_wait(5)

    url = "https://tutorialsninja.com/demo/"
    driver.get(url)
    request.cls.driver = driver

    yield
    driver.quit()
    