import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"])
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path='C:\\Users\\SatishKumar\\PycharmProjects\\OrangeHRM\\Drivers\\chromedriver.exe')
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield
    driver.quit()