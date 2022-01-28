import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["firefox"])
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.param == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = driver
    driver.implicitly_wait(100)
    driver.set_page_load_timeout(100)
    driver.maximize_window()
    yield
    driver.quit()