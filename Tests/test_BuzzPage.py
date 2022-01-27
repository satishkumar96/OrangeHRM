import time

from Pages.BuzzPage import BuzzPage
from Pages.LoginPage import LoginPage
from Tests.BaseTest import BaseTest
from Configuration.ConfiTest import init_driver

class Test_BuzzPage(BaseTest):
    def test_update_status(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        self.buzzpage = BuzzPage(self.driver)
        print("\n", "************************* CHECKING UPDATE STATUS************************************")
        time.sleep(3)
        self.buzzpage.update_status()

    def test_delete_post(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        self.buzzpage = BuzzPage(self.driver)
        print("\n", "************************* CHECKING DELETE STATUS************************************")
        time.sleep(3)
        self.buzzpage.delete_post()

    # def test_upcoming_anniversaries(self):
    #     self.loginpage = LoginPage(self.driver)
    #     self.loginpage.do_valid_login()
    #     self.buzzpage = BuzzPage(self.driver)
    #     print("\n", "************************* CHECKING UPCOMING ANNIVERSARY ************************************")
    #     time.sleep(3)
    #     self.buzzpage.upcoming_anniversary()

    def test_most_liked_post(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_valid_login()
        self.buzzpage = BuzzPage(self.driver)
        print("\n", "************************* CHECKING MOST LIKED POST ************************************")
        time.sleep(3)
        self.buzzpage.most_liked_post()

    # def test_most_commented_post(self):
    #     self.loginpage = LoginPage(self.driver)
    #     self.loginpage.do_valid_login()
    #     self.buzzpage = BuzzPage(self.driver)
    #     print("\n", "************************* CHECKING MOST COMMENTED POST ************************************")
    #     time.sleep(3)
    #     self.buzzpage.most_commented_post()