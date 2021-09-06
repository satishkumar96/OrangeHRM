from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    ADMIN = (By.ID, "menu_admin_viewAdminModule")
    PIM = (By.ID, "menu_pim_viewPimModule")
    LEAVE = (By.ID, "menu_leave_viewLeaveModule")
    TIME = (By.ID, "menu_time_viewTimeModule")
    RECRUITMENT = (By.ID, "menu_recruitment_viewRecruitmentModule")
    MY_INFO = (By.ID, "menu_pim_viewMyDetails")
    PERFORMANCE = (By.ID, "menu__Performance")
    DIRECTORY = (By.ID, "menu_directory_viewDirectory")
    MAINTENANCE = (By.ID, "menu_maintenance_purgeEmployee")

    def __init__(self, driver):
        super().__init__(driver)

    def click_elements(self):
        self.do_click(self.ADMIN)
        self.do_click(self.PIM)
        self.do_click(self.LEAVE)
        self.do_click(self.TIME)
        self.do_click(self.RECRUITMENT)
        self.do_click(self.MY_INFO)
        self.do_click(self.PERFORMANCE)
        self.do_click(self.DIRECTORY)
        self.do_click(self.MAINTENANCE)