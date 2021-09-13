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
    BUZZ = (By.ID, "menu_buzz_viewBuzz")

    COMPANY_LOGO = (By.XPATH, '//div[@id="branding"]/a/img')
    QUICK_LAUNCH = (By.XPATH, '//div[@class="quickLaunge"]')
    LEGEND_LIST = (By.XPATH, '//div[@id="div_legend_pim_employee_distribution_legend"]/table/tbody/tr')

    def __init__(self, driver):
        super().__init__(driver)

    def get_company_logo(self, HomePageCompanyLogo):
        self.get_image(self.COMPANY_LOGO, HomePageCompanyLogo)

    def get_quick_launch(self):
        self.handle_elements(self.QUICK_LAUNCH)

    def get_legends_list(self):
        self.handle_elements(self.LEGEND_LIST)

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