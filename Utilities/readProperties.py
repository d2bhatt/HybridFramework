import configparser

# to read data from config.ini file we need to create object of RawConfigParser class which contains method to read data
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")
# now to read data from files:- config.ini we need to create separate methods for each data and for that we need to
# create class


class ReadConfigData:
    # config = configparser.RawConfigParser()
    # we could have created config object inside the class but then it would become class variable and to access inside
    # method we had to use  self, but if we use self inside method than to access the method from test_login we had to
    # put self in the method bracket and it would be incorrect
    # config.read(".\\Configuration\\config.ini")

    @staticmethod         # to access the method without creating object of the class we use static method
    def getApplicationUrl():
        # def getApplicationUrl(self): using self here would result in using self in test_login while calling
        app_url = config.get('common-data', 'url')  # common-data is the category
        return app_url

    @staticmethod
    def getUsername():
        username = config.get('common-data', 'email')
        return username

    @staticmethod
    def getPassword():
        pswd = config.get('common-data', 'password')
        return pswd
