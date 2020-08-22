from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    if browser=="Chrome":
        driver=webdriver.Chrome(executable_path="C:/Users/Acer/Downloads/chromedriver_win32/chromedriver.exe")
    elif browser=="firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()
    return driver


import pytest

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

