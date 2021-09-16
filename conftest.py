import pytest
from selenium import webdriver

def pytest_addoption(parser):

    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope = "class")

def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "opera":
        driver = webdriver.Chrome(executable_path="C:\\operadriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()









