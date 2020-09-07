import time
from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddNewCustomerPage import AddNewCustomer
from Utilities.readProperties import ReadConfigData
from Utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    url = ReadConfigData.getApplicationUrl()
    email = ReadConfigData.getUsername()
    password = ReadConfigData.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_customer(self, setup):
        self.logger.info("*******************Test_003_AddCustomer*********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****************login successful************")

        self.logger.info("***************start adding customer test**********")
        self.addcustomer = AddNewCustomer(self.driver)
        self.addcustomer.click_customerMenu()
        self.addcustomer.click_CutomerMenuItem()
        self.addcustomer.click_AddNewCustomer()

        self.logger.info("**********providing customer info*************")

        self.email = random_generator() + "@gmail.com"
        self.addcustomer.setEmail(self.email)

        self.addcustomer.setPassword("test123")
        self.addcustomer.setFirstName("deepak")
        self.addcustomer.setLastName("bhatt")
        self.addcustomer.setGender("Male")
        self.addcustomer.setDOB("12/09/1999")
        self.addcustomer.setCompanyName("abc corp.")
        self.addcustomer.setCustomerRole("Guests")
        self.addcustomer.setmanagerOfVendor("Vendor 1")
        self.addcustomer.setAdminContent("testing application")

        self.addcustomer.clickOnSave()
        self.logger.info("***************saving customer info*******************")
        self.logger.info("***********add customer validation started************")
# this below statement will extract all text message inside the body
        self.message = self.driver.find_element_by_tag_name("body").text
        print(self.message)
# below statement means if the message is inside self.message
        if "The new customer has been added successfull" in self.message:
            assert True == True
            self.logger.info("*****add customer passed************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_customer_screen.png")
            self.logger.error("*******add customer test failed*****************")
            assert True == False

        self.driver.close()
        self.logger.info("*************Ending Test_003_AddCustomer**********************")

# to generate random values


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))











