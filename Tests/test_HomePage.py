from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Configuration.ConfiTest import init_driver

class Test_HomePage(BaseTest):
    def test_company_logo(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        self.homepage = HomePage(self.driver)
        self.homepage.get_company_logo("HomePageCompanyLogo")

    def test_quick_launch(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        print("****** PRINT QUICK LAUNCH LINK TEXT ******")
        self.homepage = HomePage(self.driver)
        self.homepage.get_quick_launch()

    def test_legend_list(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        print("****** PRINT QUICK LAUNCH LINK TEXT ******")
        self.homepage = HomePage(self.driver)
        self.homepage.get_legends_list()

    def test_clickable_elements(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        print("Check Elements clickable or not")
        self.homepage = HomePage(self.driver)
        print("**************** Test to check Home Page Dashboard Elelemnt is clickable or not ************************")
        self.homepage.click_elements()
