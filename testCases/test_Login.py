from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfigData
from Utilities.customLogger import LogGen


class Test_001_Login:

    # below three lines contain data  which is common so we will create a separate config.ini(initialization)
    # file under config folder where we will keep these values.This is not test data it is just prerequisite.
    # Now to read common data we would create readProperties.py utility file
    # url = "https://admin-demo.nopcommerce.com/"
    # email = "admin@yourstore.com"
    # password = "admin"
    url = ReadConfigData.getApplicationUrl()
    email = ReadConfigData.getUsername()
    password = ReadConfigData.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*********************Test_001_Login***********************")
        self.logger.info("********************Verifying Home Page Title*************")
        # self.driver = webdriver.Chrome()  # so if you see same line is repeated twice in another method
        # so we keep them in conftest files so these fixtures are repeated.So this has to be done everytime before
        # automating browser
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        actual_title = self.driver.title

        if actual_title == "Your store Login":
            assert True
            self.logger.warning("*******************home_page_title is passed*********")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_home_page_title.png")
            self.driver.close()
            self.logger.error("*******************home_page_title is failed*********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("*******************verifying login Page*********")
        self.driver = setup
        # self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*****************login test is passed*************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")  # dot represents current project
            # directory, name of the screen shot should be as the test case name
            self.driver.close()
            self.logger.error("*****************login test is failed*************")
            assert False


# to run pytest -v -s testCases/test_Login.py
# pytest -v -s -n=2 testCases/test_Login.py
# pytest -v -s -n=2 testCases/test_Login.py --browser chrome
# pytest -v -s -n=2 --html=Reports/report.html testCases/test_Login.py --browser chrome
# if list_status contains only pass value than the test case is passed otherwise test case is failed
# cls for clearing the screen

