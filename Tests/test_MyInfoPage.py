from Pages.LoginPage import LoginPage
from Pages.MyInfoPage import MyInfoPage
from Tests.BaseTest import BaseTest
from Configuration.ConfiTest import init_driver

class Test_MyInfo(BaseTest):
    # def test_blood_type(self):
    #     self.loginpage = LoginPage(self.driver)
    #     self.loginpage.do_valid_login()
    #     self.myinfopage = MyInfoPage(self.driver)
    #     self.myinfopage.blood_type()

    def test_add_attachements(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        self.myinfopage = MyInfoPage(self.driver)
        self.myinfopage.add_attachements()

    def test_delete_attachements(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        self.myinfopage = MyInfoPage(self.driver)
        self.myinfopage.delete_attachement()

    def test_edit_profile(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        self.myinfopage = MyInfoPage(self.driver)
        self.myinfopage.edit_profile()