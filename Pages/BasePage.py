
import urllib.request

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from Configuration.DataFromExcel import TestData


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.URL)

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
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
        Select(element).select_by_visible_text(text)

    def action_click(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def handle_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(by_locator))
        for elem in elements:
            print("\n", elem.text)

    def get_image(self, by_locator, imageName):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
        urllib.request.urlretrieve(element.get_attribute('src'),imageName)
        img = Image.open(imageName)
        img.show()

    def get_link_value(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
        return element.get_attribute('href')