import time
from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.AddNewCustomerPage import AddNewCustomer
from Utilities.readProperties import ReadConfigData
from Utilities.customLogger import LogGen


class Test_004_SearchCustomer:
    url = ReadConfigData.getApplicationUrl()
    email = ReadConfigData.getUsername()
    password = ReadConfigData.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("*******************Test_004_SearchCustomer*********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****************login successful************")

        self.logger.info("***************start search customer by email**********")
        self.addcustomer = AddNewCustomer(self.driver)
        self.addcustomer.click_customerMenu()
        self.addcustomer.click_CutomerMenuItem()

        self.logger.info("**********searching by customer email id*************")
        searchcustomer = SearchCustomer(self.driver)
        searchcustomer.set_email("victoria_victoria@nopCommerce.com")
        searchcustomer.click_search()
        time.sleep(5)

        status = searchcustomer.search_customer_by_email("victoria_victoria@nopCommerce.com")
        assert True == status
        self.driver.close()
        self.logger.info("*************Ending Test_004_SearchCustomerByEmail**********************")
#   pytest -v -s --html=Reports/report.html testCases/test_searchCustomer.py --browser chrome
#   pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --browser chrome  (here m is marker for sanity/reg)
#   pytest -v -s -m "regression" --html=Reports/report.html testCases/ --browser chrome
#   pytest -v -s -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
#   pytest -v -s -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome
#   now to run through bat file create run.bat file at location C:\Users\neha_bhatt\PycharmProjects\HybridFramework
# rem in bat file is to comment the command line.now to run the bat file first place the code at bat file.second open
# command prompt as admin and double click bat file.












