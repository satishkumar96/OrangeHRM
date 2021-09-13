from selenium.webdriver.common.by import By

from Configuration.DataFromExcel import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "txtUsername")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BTN = (By.ID, "btnLogin")
    USER_PROFILE = (By.ID, "welcome")
    LOGOUT = (By.XPATH, "//a[text()='Logout']")
    ERROR_MSG = (By.XPATH, "//div[@id='divLoginButton']/span")
    COMPANY_LOGO = (By.XPATH, "//*[@id='divLogo']/img")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//div[@id='forgotPasswordLink']/a")

    def __init__(self, driver):
        super().__init__(driver)

    def get_company_logo(self, LoginPageCompanyLogo):
        self.get_image(self.COMPANY_LOGO, LoginPageCompanyLogo)

    def get_forgot_password_link(self):
        print("\n",self.get_link_value(self.FORGOT_PASSWORD_LINK))

    def do_valid_login(self):
        self.do_clear(self.USERNAME)
        self.do_sendKeys(self.USERNAME, TestData.USERNAME)
        self.do_clear(self.PASSWORD)
        self.do_sendKeys(self.PASSWORD, TestData.PASSWORD)
        self.do_click(self.LOGIN_BTN)
        self.do_click(self.USER_PROFILE)

    def do_invalid_login(self):
        self.do_clear(self.USERNAME)
        self.do_sendKeys(self.USERNAME, "Admi")
        self.do_clear(self.PASSWORD)
        self.do_sendKeys(self.PASSWORD, "adm")
        self.do_click(self.LOGIN_BTN)
        self.get_element_text(self.ERROR_MSG)

    def do_blank_login(self):
        self.do_clear(self.USERNAME)
        self.do_sendKeys(self.USERNAME, "")
        self.do_clear(self.PASSWORD)
        self.do_sendKeys(self.PASSWORD, "")
        self.do_click(self.LOGIN_BTN)
        self.get_element_text(self.ERROR_MSG)

    def do_blank_username(self):
        self.do_clear(self.USERNAME)
        self.do_sendKeys(self.USERNAME, "")
        self.do_clear(self.PASSWORD)
        self.do_sendKeys(self.PASSWORD, TestData.PASSWORD)
        self.do_click(self.LOGIN_BTN)
        self.get_element_text(self.ERROR_MSG)

    def do_blank_password(self):
        self.do_clear(self.USERNAME)
        self.do_sendKeys(self.USERNAME, TestData.USERNAME)
        self.do_clear(self.PASSWORD)
        self.do_sendKeys(self.PASSWORD, "")
        self.do_click(self.LOGIN_BTN)
        self.get_element_text(self.ERROR_MSG)
