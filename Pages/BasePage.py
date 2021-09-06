from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.readData_fromExcel("D:\TestData.xlsx", "MyInfo", 1, 2))

    def do_sendKeys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).click()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
        return element.text

    def do_clear(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).clear()

    def select_by_text(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        Select(element).select_by_visible_text(text)

    def action_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def readData_fromExcel(self, file, sheetname, rownum, colnum):
        workbook = openpyxl.load_workbook(file)
        sheet = workbook[sheetname]
        inputvalue = sheet.cell(row=rownum, column=colnum).value
        return inputvalue
