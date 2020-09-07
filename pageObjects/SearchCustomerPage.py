class SearchCustomer:

    textbox_email_id = "SearchEmail"
    textbox_FirstName_id = "SearchFirstName"
    textbox_LastName_id = "SearchLastName"
    button_Search_id = "search-customers"

    table_gridResult_xpath = "//table[@id='customers-grid']"
    table_row_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_element_by_id(self.textbox_FirstName_id).clear()
        self.driver.find_element_by_id(self.textbox_FirstName_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_id(self.textbox_LastName_id).clear()
        self.driver.find_element_by_id(self.textbox_LastName_id).send_keys(last_name)

    def click_search(self):
        self.driver.find_element_by_id(self.button_Search_id).click()

    def get_number_of_rows(self):
        row_length = len(self.driver.find_elements_by_xpath(self.table_row_xpath)) # more than 1 row that's why elements
        print(row_length)
        return row_length

    def get_number_of_columns(self):
        return len(self.driver.find_elements_by_xpath(self.table_column_xpath)) # more than 1 col that's why elements

    def search_customer_by_email(self, email):

        # now here we have to check that email id which we get in result is equal to email which we are searching for
        # that we have to run loop to search email in each row

        flag = False
        for r in range(1, self.get_number_of_rows()+1):
            # to check the email we have to go to table grid result then inside the table we have to check mail
            table = self.driver.find_element_by_xpath(self.table_gridResult_xpath)
            email_id = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text

            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, name):

        # now here we have to check that email id which we get in result is equal to email which we are searching for
        # that we have to run loop to search email in each row

        flag = False
        for r in range(1, self.get_number_of_rows()+1):
            table = self.driver.find_element_by_xpath(self.table_gridResult_xpath)
            search_result_name = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text

            if search_result_name == name:
                flag = True
                break
        return flag











