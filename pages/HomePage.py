from selenium import webdriver
from selenium.webdriver.support.select import Select


class HomePage:
    text_name_xpath="//div[@class='form-group']//input[@name='name']"
    text_email_name="email"
    text_password_id="exampleInputPassword1"
    select_gender_id="exampleFormControlSelect1"
    click_radio_id="inlineRadio1"
    text_dob_xpath="//input[@name='bday']"
    btn_submit_xpath="//input[@class='btn btn-success']"

    def __init__(self,driver):
        self.driver=driver

    def set_Name(self,username):
        self.driver.find_element_by_xpath(self.text_name_xpath).send_keys(username)

    def set_Email(self,email):
        self.driver.find_element_by_name(self.text_email_name).send_keys(email)

    def set_password(self,password):
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def set_Gender(self):
        ele=self.driver.find_element_by_id(self.select_gender_id)
        drp=Select(ele)
        drp.select_by_index(1)


    def set_DOB(self,date):
        self.driver.find_element_by_xpath(self.text_dob_xpath).send_keys(date)

    def Click_Sbt(self):
        self.driver.find_element_by_xpath(self.btn_submit_xpath).click()



