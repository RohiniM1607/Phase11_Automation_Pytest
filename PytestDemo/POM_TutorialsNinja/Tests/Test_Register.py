import pytest
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage
from Utilities import ExcelReader

@pytest.mark.parametrize("firstname, lastname, email, telephone, password, confirmpassword", ExcelReader.get_data("ExcelFiles/TestData.xlsx", "Register"))
@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_Register(self, firstname, lastname, email, telephone, password, confirmpassword):
        logger = Lo                                                                                                                                                                                                                                                                                                                                                              
        home_page = HomePage(self.driver)
        register_page = RegisterPage(self.driver)
        home_page.click_Register()
        register_page.enter_details(firstname, lastname, email, telephone, password, confirmpassword)

        try:
            success_msg = register_page.get_success_message()
            assert success_msg == "Your Account Has Been Created!"
            print("Registration Successful")

        except:
            error_msg = register_page.get_error_message()
            print("Registration Failed:", error_msg)
            assert "Warning" in error_msg