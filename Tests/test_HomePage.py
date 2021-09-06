from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Configuration.ConfiTest import init_driver

class Test_HomePage(BaseTest):
    def test_clickable_elements(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        print("Check Elements clickable or not")
        self.homepage = HomePage(self.driver)
        self.homepage.click_elements()