import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["firefox", "chrome"])
def init_driver(request):
    if request.param == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    if request.param == "firefox":
        service = FirefoxService(executable_path='Drivers/geckodriver.exe')
        driver = webdriver.Firefox(service=service)
    request.cls.driver = driver
    driver.implicitly_wait(100)
    driver.set_page_load_timeout(100)
    driver.delete_all_cookies()
    driver.maximize_window()
    yield
    driver.quit()

    """Clean up the HTML directory to generate new HTML report"""
    folder = 'HTML_Reports'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))