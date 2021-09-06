from Pages.LoginPage import LoginPage
from Pages.UserPage import UserPage
from Tests.BaseTest import BaseTest
from Configuration.ConfiTest import init_driver


class Test_UserPage(BaseTest):
    def test_delete_module(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        self.userpage = UserPage(self.driver)
        self.userpage.delete_first_row()