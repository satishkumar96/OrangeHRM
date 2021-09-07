import time

from selenium.webdriver.common.by import By
import rpa

from Configuration.DataFromExcel import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class MyInfoPage(BasePage):

    BLOOD_TYPE = (By.NAME, "custom1")
    EDIT_BUTTON = (By.ID, "btnEditCustom")
    ADD_ATTACHEMENT = (By.ID, "btnAddAttachment")
    SAVE_ATTACHEMENT = (By.ID, "btnSaveAttachment")
    RECENT_UPLOAD_ATTACHEMENT = (By.XPATH, "//table[@id='tblAttachments']/tbody/tr/td[2]")
    RECENT_UPLOAD_ATTACHEMENT_CHCKBOX = (By.XPATH, "//table[@id='tblAttachments']/tbody/tr[1]/td[1]/input")
    DELETE_BUTTON = (By.ID, "btnDeleteAttachment")
    CHOOSE_FILE = (By.XPATH, "//li[@class='fieldHelpContainer']/input[2]")
    SUCCESS_DELETE = (By.XPATH, "(//div[@class='modal-body'])[2]/div[4]")
    EDIT_PROFILE_BUTTON = (By.ID, "btnSave")

    """Personal Details"""
    FIRST_NAME = (By.ID, "personal_txtEmpFirstName")
    MIDDLE_NAME = (By.ID, "personal_txtEmpMiddleName")
    LAST_NAME = (By.ID, "personal_txtEmpLastName")
    EMPLOYEE_ID = (By.ID, "personal_txtEmployeeId")
    OTHERS_ID = (By.ID, "personal_txtOtherID")
    DRIVER_LICENSE_NUMBER = (By.ID, "personal_txtLicenNo")
    SSN_NUMBER = (By.ID, "personal_txtNICNo")
    SIN_NUMBER = (By.ID, "personal_txtSINNo")
    NICK_NAME = (By.ID, "personal_txtEmpNickName")
    MILITARY_SERVICE = (By.ID, "personal_txtMilitarySer")
    GENDER_MALE = (By.XPATH, "//li[@class='radio']/ul/li[1]/input")
    GENDER_FEMALE = (By.XPATH, "//li[@class='radio']/ul/li[2]/input")
    MARTIAL_STATUS = (By.ID , "personal_cmbMarital")
    NATIONALITY = (By.ID, "personal_cmbNation")
    SMOKER = (By.NAME, "personal[chkSmokeFlag]")

    def __init__(self, driver):
        super().__init__(driver)

    def blood_type(self):
        self.do_click(HomePage.MY_INFO)
        self.do_click(self.EDIT_BUTTON)
        self.select_by_text(self.BLOOD_TYPE, "B+")
        self.do_click(self.EDIT_BUTTON)

    def add_attachements(self):
        self.do_click(HomePage.MY_INFO)
        self.do_click(self.ADD_ATTACHEMENT)
        time.sleep(3)
        self.action_click(self.CHOOSE_FILE)
        rpa.init(visual_automation=True, chrome_browser=False)
        rpa.type("C:\\Users\\SatishKumar\\PycharmProjects\\OrangeHRM\\element_Images\\File_Name.png",
                 "C:\\Users\\SatishKumar\\Downloads\\jmeter.log[enter]")
        rpa.close()
        self.do_click(self.SAVE_ATTACHEMENT)
        print("\n", self.get_element_text(self.RECENT_UPLOAD_ATTACHEMENT))

    def delete_attachement(self):
        self.do_click(HomePage.MY_INFO)
        self.do_click(self.RECENT_UPLOAD_ATTACHEMENT_CHCKBOX)
        self.do_click(self.DELETE_BUTTON)
        print(self.get_element_text(self.SUCCESS_DELETE))

    def edit_profile(self):
        self.do_click(HomePage.MY_INFO)
        self.do_click(self.EDIT_PROFILE_BUTTON)
        self.do_clear(self.FIRST_NAME)
        self.do_sendKeys(self.FIRST_NAME, TestData.FIRST_NAME)
        self.do_clear(self.MIDDLE_NAME)
        self.do_sendKeys(self.MIDDLE_NAME, TestData.MIDDLE_NAME)
        self.do_clear(self.LAST_NAME)
        self.do_sendKeys(self.LAST_NAME, TestData.LAST_NAME)
        self.do_clear(self.EMPLOYEE_ID)
        self.do_sendKeys(self.EMPLOYEE_ID, TestData.EMPLOYEE_ID)
        self.do_clear(self.OTHERS_ID)
        self.do_sendKeys(self.OTHERS_ID, TestData.OTHERS_ID)
        self.do_clear(self.DRIVER_LICENSE_NUMBER)
        self.do_sendKeys(self.DRIVER_LICENSE_NUMBER, TestData.DRIVER_LICENSE_NUMBER)
        self.do_clear(self.SSN_NUMBER)
        self.do_sendKeys(self.SSN_NUMBER, TestData.SSN_NUMBER)
        self.do_clear(self.SIN_NUMBER)
        self.do_sendKeys(self.SIN_NUMBER, TestData.SIN_NUMBER)
        self.do_clear(self.MILITARY_SERVICE)
        self.do_sendKeys(self.MILITARY_SERVICE, TestData.MILITARY_SERVICE)
        self.select_by_text(self.MARTIAL_STATUS, TestData.MARTIAL_STATUS)
        self.select_by_text(self.NATIONALITY, TestData.NATIONALITY)

        """Check Gender"""
        if TestData.GENDER == "Male":
            self.do_click(self.GENDER_MALE)
        elif TestData.GENDER == "Female":
            self.do_click(self.GENDER_FEMALE)
        else:
            print("Wrong Input")

        """Check for Smoker"""
        if TestData.SMOKER == "Yes":
            self.do_click(self.SMOKER)
        self.do_click(self.EDIT_PROFILE_BUTTON)