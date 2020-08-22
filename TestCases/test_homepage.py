from selenium import webdriver
import pytest
from selenium.webdriver.support import select
from pages.HomePage import HomePage
from Utilities.readrequirement import Readconfig


class Test_001_homePage:
    url = Readconfig.getapplicationURL()
    Name = Readconfig.getName()
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    DOB = Readconfig.getDOB()

    def test_homePage(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        title = self.driver.title
        if title == "ProtoCommerce":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("C:/Users/Acer/PycharmProjects/npncommerce/screenshots/logs.png")
            self.driver.close()
            assert False

    def test_registration(self,setup):
        self.driver= setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.hp.set_Name(self.Name)
        self.hp.set_Email(self.Email)
        self.hp.set_password(self.Password)
        self.hp.set_Gender()
        self.hp.set_DOB(self.DOB)
        self.hp.Click_Sbt()
        confirm=self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
        self.driver.close()
        assert "Success! The Form has been submitted successfully!." in confirm








