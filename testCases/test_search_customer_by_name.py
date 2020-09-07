import time
from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.AddNewCustomerPage import AddNewCustomer
from Utilities.readProperties import ReadConfigData
from Utilities.customLogger import LogGen


class Test_005_SearchCustomer:
    url = ReadConfigData.getApplicationUrl()
    email = ReadConfigData.getUsername()
    password = ReadConfigData.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.logger.info("*******************Test_004_SearchCustomer*********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****************login successful************")

        self.logger.info("***************start search customer by name**********")
        self.addcustomer = AddNewCustomer(self.driver)
        self.addcustomer.click_customerMenu()
        self.addcustomer.click_CutomerMenuItem()

        self.logger.info("**********searching by customer name*************")
        searchcustomer = SearchCustomer(self.driver)
        searchcustomer.set_first_name("Victoria")
        searchcustomer.set_last_name("Terces")
        searchcustomer.click_search()
        time.sleep(5)

        status = searchcustomer.search_customer_by_name("Victoria Terces")
        assert True == status
        self.driver.close()
        self.logger.info("*************Ending Test_004_SearchCustomerByName**********************")
#   pytest -v -s --html=Reports/report.html testCases/test_search_customer_by_name.py --browser chrome












