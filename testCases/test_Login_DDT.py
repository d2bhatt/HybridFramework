from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfigData
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import time


class Test_002_DDT_Login:

    # below three lines contain data  which is common so we will create a separate config.ini(initialization)
    # file under config folder where we will keep these values.This is not test data it is just prerequisite.
    # Now to read common data we would create readProperties.py utility file
    # url = "https://admin-demo.nopcommerce.com/"
    # email = "admin@yourstore.com"
    # password = "admin"
    url = ReadConfigData.getApplicationUrl()

    file_path = ".//TestData/Login_Data.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*********************Test_002_DDT_Login***********************")
        self.logger.info("*******************verifying login Page*********")
        self.driver = setup
        # self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.file_path, 'Sheet1')
        print("number of rows:", self.rows)

        list_status = []
        for r in range(2, self.rows+1):
            self.username = XLUtils.readData(self.file_path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.file_path, 'Sheet1', r, 2)
            self.status = XLUtils.readData(self.file_path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            # 1 scenario:- invalid credentials user is able to login and actual title would be equal to expected title
            # so in this case expected column would be fail but in actual it is pass
            # 2 scenario:- with valid credentials user is not able to login
# in below case with valid credentials expected == actual title, and status in excel would be equivalent to pass
# also if we have a list which contains values which stores the results as pass when all negative/positive
# combinations are tried list=[pass,pass,pass] ; expected=[pass,fail ,fail]. suppose if any value is fail in list
# than whole list is fail, so every value should be pass in list
            # case1: valid credentials
            if actual_title == expected_title:
                if self.status == "pass":
                    self.logger.info("******passed_1*********")
                    self.lp.clickLogout()
                    list_status.append("pass")
            # case2:-with invalid credentials user is able to login
                elif self.status == "fail": # when titles are matching but according to excel it should have failed
                    self.logger.info("************failed_1***********")
                    self.lp.clickLogout()
                    list_status.append("fail")
            # case3:- with valid credentials user is not able to login
            elif actual_title != expected_title:
                if self.status == "pass":  # here self.status means expected in excel matches pass value
                    self.logger.info("****failed_2*****")
                    list_status.append("fail")

            # case4:- with invalid credentials user is not able to login
                elif self.status == "fail":
                    self.logger.info("*****passed_2******")
                    list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("***********passed_3*************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****failed_3***********")
            self.driver.close()
            assert False

        self.logger.info("***************END OF DATA DRIVEN TESTING**********")
        self.logger.info("*************end of tc002************")

# to run pytest -v -s testCases/test_Login_DDT.py
# pytest -v -s -n=1 testCases/test_Login_DDT.py
# pytest -v -s testCases/test_Login_DDT.py --browser chrome
# pytest -v -s -n=1 --html=Reports/report.html testCases/test_Login_DDT.py --browser chrome

