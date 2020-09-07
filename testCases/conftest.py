import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\seleniumDrivers\\chromedriver_win32 (1)\\chromedriver.exe")
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\seleniumDrivers\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Ie(executable_path="C:\\seleniumDrivers\\IEDriverServer_x64_3.150.1\\IEDriverServer.exe")
        print("Launching ie browser..............")
    return driver
# to run tests on desired browser from command line


def pytest_addoption(parser):  # this will get value from command line(name of method is addoption )
    parser.addoption("--browser")  # getting the browser name from command line into the variable --browser


@pytest.fixture()
def browser(request):  # this will return browser value to the setup method
    return request.config.getoption("--browser")

# to run test on desired browser:- pytest -v -s testCases/test_Login.py --browser chrome
# to run test parallel we can give maximum value as 3:- pytest -v -s -n=2 testCases/test_Login.py --browser chrome;
# where n= 2 is the two methods or tests will run parallel


# ############## pytest html report####################################################

# it is hook for adding environment info to HTML report
# A hook is a means of executing custom code (function) either before, after, or instead of existing code.
# For example, a function may be written to "hook" into the login process in order to execute a Captcha function
# before continuing on to the normal login process
def pytest_configure(config):
    config._metadata['Project Name'] = 'Hybrid Framework'
    config._metadata['Module Name'] = 'Admin'
    config._metadata['Tester'] = 'Deepak'


# It is hook for delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# pytest -v -s -n=2 --html=Reports\report.html testCases/test_Login.py --browser chrome
