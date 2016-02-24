import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ApartmentLoginTestCase(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        # self.driver = webdriver.Firefox()
        chromedriver = "chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get("http://127.0.0.1:8000/apartmentApp/")
        # self.driver.get("http://apartment-app.pfsa2harbh.us-west-2.elasticbeanstalk.com/apartmentApp")

    def test_login(self):
        #make sure we are in the home page
        username = "jourey"
        password = "test"
        #username
        name = self.driver.find_element_by_name("username")
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        name.send_keys(username)
        #password
        passfield = self.driver.find_element_by_name("password")
        passfield.send_keys(Keys.CONTROL + "a")
        passfield.send_keys(Keys.DELETE)
        passfield.send_keys(password)
        #submit button
        submit = '//input[@type="submit" and @value="Login"]'
        submitButton = self.driver.find_element_by_xpath(submit)
        submitButton.click()

    def tearDown(self):
        self.driver.close()


#run the tests
if __name__ == "__main__":
    unittest.main()