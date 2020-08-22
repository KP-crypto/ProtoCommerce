from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path="C:/Users/Acer/Downloads/chromedriver_win32/chromedriver.exe")
    return driver

