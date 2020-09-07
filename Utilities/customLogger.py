# Python has a built-in module logging which allows writing status messages to a file or any other output streams.
# The file can contain the information on which part of the code is executed and what problems have been arisen.
import logging
# so as to read logs from applcation we create custom logger file , so all the actions would be performed inside a
# method which would be called later and this method would be inside a class


class LogGen:

    @staticmethod
    def loggen():  # removing self as this would be static method and can called without creating object

        for handler in logging.root.handlers[:]: logging.root.removeHandler(handler)

        logging.basicConfig(filename=".\\Logs\\automation.log",
                                     format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%y %I:%M:%S %p'
                            # to have time stamp date format in other way-date(mmm/dd/yy) time
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

# logging.DEBUG would return detailed information
# Debug : These are used to give Detailed information
# Info : These are used to Confirm that things are working as expected
# Warning :These are used an indication that something unexpected happened, or indicative of some problem in near future
# Error : This tells that due to a more serious problem, the software has not been able to perform some function
# Critical : This tells serious error, indicating that the program itself may be unable to continue running
