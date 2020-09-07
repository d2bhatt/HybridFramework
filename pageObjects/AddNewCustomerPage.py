import time
from selenium.webdriver.support.ui import Select
# for each page element we need to write locator and action methods

class AddNewCustomer:

    link_customerMenu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    link_CutomerMenuItem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    button_AddNewCustomer_xpath = "//a[@class='btn bg-blue']"
    textbox_email_xpath = "//input[@id ='Email']"
    textbox_password_xpath = "//input[@id ='Password']"
    textbox_firstName_xpath = "//input[@id ='FirstName']"
    textbox_lastNme_xpath = "//input[@id ='LastName']"
    radiobutton_GenderMale_id = "Gender_Male"
    radiobutton_GenderFemale_id = "Gender_Female"
    textbox_DOB_xpath = "//input[@id='DateOfBirth']"
    textbox_companyName_xpath = "//input[@id= 'Company']"
    textbox_customerRoles_id = "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    listItem_administrators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']//li[1]"
    listItem_ForumModerators_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']//li[2]"
    listItem_Guests_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']//li[3]"
    listItem_Registered_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']//li[4]"
    listItem_Vendors_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']//li[5]"
    dropdown_managerOfVendor_xpath = "//*[@id ='VendorId']"
    textbox_adminComment_xpath = "//textarea[@id ='AdminComment']"
    button_save_xpath = "//button[@name ='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_customerMenu(self):
        self.driver.find_element_by_xpath(self.link_customerMenu_xpath).click()

    def click_CutomerMenuItem(self):
        self.driver.find_element_by_xpath(self.link_CutomerMenuItem_xpath).click()

    def click_AddNewCustomer(self):
        self.driver.find_element_by_xpath(self.button_AddNewCustomer_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def setmanagerOfVendor(self, value):
        dropdown_managerOfVendor = self.driver.find_element_by_xpath(self.dropdown_managerOfVendor_xpath)
        dropdown = Select(dropdown_managerOfVendor)
        dropdown.select_by_visible_text(value)

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.textbox_firstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.textbox_lastNme_xpath).send_keys(lname)

    def setDOB(self, dob):
        self.driver.find_element_by_xpath(self.textbox_DOB_xpath).send_keys(dob)

    def setCompanyName(self, company):
        self.driver.find_element_by_xpath(self.textbox_companyName_xpath).send_keys(company)

    def setAdminContent(self, admin_text):
        self.driver.find_element_by_xpath(self.textbox_adminComment_xpath).send_keys(admin_text)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.radiobutton_GenderMale_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.radiobutton_GenderFemale_id).click()
        else:
            self.driver.find_element_by_id(self.radiobutton_GenderMale_id).click()

    def setCustomerRole(self, role):
        self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
        self.driver.find_element_by_xpath(self.textbox_customerRoles_id).click()
        time.sleep(2)
        # since role registered is already selected so no need to click on it
        if role == 'Registered':
            self.lisiItem = self.driver.find_element_by_xpath(self.listItem_Registered_xpath)
        # since registered is already there so no need to click it again as it will remove the registered
        # difference b/w list and dropdown is in list -->list of items are visible
        # while in dropdown we have to click on
# dropdown button to select available item. also by just using click command we cannot execute script we have to use
# JAVASCRIPT to select from the list
        elif role == 'Administrators':
            self.lisiItem = self.driver.find_element_by_xpath(self.listItem_administrators_xpath)
        elif role == 'Guests':
            #  now if role is guest than it cannot be registered so we have to remove registered which is automatically
            # registered
            time.sleep(5)
            # self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.lisiItem = self.driver.find_element_by_xpath(self.listItem_Guests_xpath)
        elif role == 'Vendors':
            self.lisiItem = self.driver.find_element_by_xpath(self.listItem_Vendors_xpath)
        elif role == 'ForumModerators':
            self.lisiItem = self.driver.find_element_by_xpath(self.listItem_ForumModerators_xpath)
        else:
            self.lisiItem = self.driver.find_element_by_xpath(self.listItem_Guests_xpath)
        time.sleep(5)
        # javascript
        # self.listItem.click() is not working over here that's why the JS
        self.driver.execute_script("arguments[0].click();", self.lisiItem)  # JAVA SCRIPT if click not works


# to run--> pytest -v -s --html=Reports/report.html testCases/test_addCustomer.py --browser chrome



