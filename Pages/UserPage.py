import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class UserPage(BasePage):
    ADD_BUTTON = (By.ID, "btnAdd")
    DELETE_BUTTON = (By.ID, "btnDelete")
    FIRST_ROW_CHCKBOX = (By.XPATH, "//table[@id='resultTable']/tbody/tr[1]/td[1]/input")
    OK_BUTTON = (By.ID, "dialogDeleteBtn")
    FIRST_ROW_USERNAME = (By.XPATH, "//table[@id='resultTable']/tbody/tr[1]/td[2]/a")
    USERNAME_DASHBOARD = (By.LINK_TEXT, "Username")

    def __init__(self, driver):
        super().__init__(driver)

    def delete_first_row(self):
        self.do_click(HomePage.ADMIN)
        self.do_click(self.USERNAME_DASHBOARD)
        self.do_click(self.USERNAME_DASHBOARD)
        first_row_username = self.get_element_text(self.FIRST_ROW_USERNAME)
        print("\n", first_row_username)
        self.do_click(self.FIRST_ROW_CHCKBOX)
        self.do_click(self.DELETE_BUTTON)
        self.do_click(self.OK_BUTTON)
        time.sleep(3)
        if first_row_username == self.get_element_text(self.FIRST_ROW_USERNAME):
            print("Record Deleted Unsuccessful")
        else:
            print("Record Deleted Successful")
