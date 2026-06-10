from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
class SearchPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
    locators = {
        'display_status_of_valid_product': ('xpath', "//a[text()='HP LP3065]")

    }
    def get_display_status_of_valid_product(self):
        displayed_product = self.display_status_of_valid_product.get_text()
        assert displayed_product == "HP LP3065"
        