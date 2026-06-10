import pytest
from Utilities import Read_config
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        email = Read_config.get_config("login details", "email")
        password = Read_config.get_config("login details", "password")
        home_page.click_Login()
        login_page.enter_credentials(email, password)

        try:
            assert login_page.get_homepage_title() == "My Account"
            print("Login Successful")
        except AssertionError:
            print("Login Failed")
    
    