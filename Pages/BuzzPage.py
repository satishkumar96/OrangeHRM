import time

import rpa
from selenium.webdriver.common.by import By

from Configuration.DataFromExcel import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class BuzzPage(BasePage):
    UPDATE_STATUS = (By.NAME, "createPost[content]")
    POST_BUTTON = (By.ID, "postSubmitBtn")
    UPLOAD_IMAGE = (By.ID, "images-tab-label")
    UPLOAD_IMAGE_TEXT = (By.XPATH, '//*[@id="phototext"]')
    UPLOAD_IMAGE_BUTTON = (By.ID, "image-upload-button")
    UPLOAD_IMAGE_POST_BUTTON = (By.ID, "imageUploadBtn")
    RECENT_UPDATED_POST = (By.XPATH, "(//li[@class='singlePost'])[1]/div[1]/div[5]/div")
    DROPDOWN = (By.XPATH, "(//li[@class='singlePost'])[1]/div[1]/div[1]/div[3]/div")
    DELETE_DROPDOWN = (By.XPATH, "//a[text()='Delete']")
    YES_BUTTON = (By.ID, "delete_confirm")
    DELETED_SUCCESS = (By.XPATH, "//div[@id='successDataModal']/div/div[4]")
    UPCOMING_ANNIVERSARY = (By.XPATH, "//div[@id='rightBarHeadingAnniv']")
    LIST_UPCOMING_ANNIVERSARY = (By.XPATH, "//li[@id='anniversaryPost']")
    MOST_LIKED_POST = (By.ID, "rightBarHeadingMl")
    LIST_MOST_LIKED_POST = (By.XPATH, '//div[@class="birthdayUserName"]')
    MOST_COMMENTED_POST = (By.ID, "rightBarHeadingMc")
    LIST_MOST_COMMENTED_POST = (By.XPATH, '//div[@class="birthdayUserName"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.do_click(HomePage.BUZZ)

    def update_status(self):
        self.do_sendKeys(self.UPDATE_STATUS, TestData.UPDATE_STATUS)
        self.do_click(self.POST_BUTTON)
        time.sleep(3)
        print("\n", self.get_element_text(self.RECENT_UPDATED_POST))
        print("\n", "POST UPDATED SUCCESSFULLY")

    def upload_images(self):
        time.sleep(3)
        self.do_click(self.UPLOAD_IMAGE)
        time.sleep(3)
        self.do_click(self.UPLOAD_IMAGE_TEXT)
        time.sleep(3)
        self.do_sendKeys(self.UPLOAD_IMAGE_TEXT, TestData.UPDATE_STATUS)
        self.do_click(self.UPLOAD_IMAGE_BUTTON)
        rpa.init(headless_mode=True)
        rpa.type("C:\\Users\\SatishKumar\\PycharmProjects\\OrangeHRM\\element_Images\\File_Name.png",
                 "D:\\Test_Images\\48834.jpg[enter]")
        rpa.close()
        self.do_click(self.UPLOAD_IMAGE_POST_BUTTON)
        print("\n", self.get_element_text(self.RECENT_UPDATED_POST))
        print("\n", "IMAGE UPLOADED SUCCESSFULLY")

    def delete_post(self):
        self.do_click(self.DROPDOWN)
        time.sleep(1)
        self.do_click(self.DELETE_DROPDOWN)
        time.sleep(1)
        self.do_click(self.YES_BUTTON)
        print(self.get_element_text(self.DELETED_SUCCESS))

    def upcoming_anniversary(self):
        self.do_click(self.UPCOMING_ANNIVERSARY)
        time.sleep(3)
        self.handle_elements(self.LIST_UPCOMING_ANNIVERSARY)

    def most_liked_post(self):
        self.do_click(self.MOST_LIKED_POST)
        time.sleep(3)
        self.handle_elements(self.LIST_MOST_LIKED_POST)

    def most_commented_post(self):
        self.do_click(self.MOST_COMMENTED_POST)
        time.sleep(3)
        self.handle_elements(self.LIST_MOST_COMMENTED_POST)