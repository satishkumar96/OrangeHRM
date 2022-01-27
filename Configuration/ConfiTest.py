import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager


@pytest.fixture(params=["chrome"])
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "opera":
        driver = webdriver.Opera(OperaDriverManager().install())
    request.cls.driver = driver
    driver.implicitly_wait(100)
    driver.set_page_load_timeout(100)
    driver.maximize_window()
    yield
    driver.quit()