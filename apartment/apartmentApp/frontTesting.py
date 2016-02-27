import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ApartmentLoginTestCase(unittest.TestCase):
    """Test Case for logging into the app"""

    def setUp(self):
        """
        if your browser is chrome,change self.driver = webdriver.Firefox() to the follows
        chromedriver = "chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        """
        # if the browser if Firefox
        self.driver = webdriver.Firefox()
        self.driver.get("http://127.0.0.1:8000/apartmentApp/")

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

class ApartmentSendMessageTestCase(unittest.TestCase):
    """Test Case for sending messages to a test user"""
    def setUp(self):

        """
        if your browser is chrome,change self.driver = webdriver.Firefox() to the follows
        chromedriver = "chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        """
        # self.driver.get("http://apartment-app.pfsa2harbh.us-west-2.elasticbeanstalk.com/apartmentApp")
        self.driver = webdriver.Firefox()

    def test_sending_messages(self):
        #make sure we are in the home page
        # the url should be changed to create message url
        self.driver.get("file:///Users/caoqing/Desktop/COMP4350/apartment/messaging/templates/createMessage.html")
        username = "jourey"
        msg = "test message from selenium"
        urg = "1"
        #username
        name = self.driver.find_element_by_name("name")
        name.send_keys(username)
        #message
        message = self.driver.find_element_by_name("message")
        message.send_keys(msg)
        #urgency
        urgency = self.driver.find_element_by_name("urgency")
        urgency.send_keys(urg)
        #submit button
        send = '//input[@type="submit" and @value="Send"]'
        sendButton = self.driver.find_element_by_xpath(send)
        sendButton.click()
        self.driver.close()



class ApartmentBulletinBoardTestCase(unittest.TestCase):

    def setUp(self):
        """
        if your browser is chrome,change self.driver = webdriver.Firefox() to the follows
        chromedriver = "chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        """

        self.driver = webdriver.Firefox()


    def test_jump_from_bulletin_board_to_create_new_bulletin_page(self):
        # url should be changed to bulletin board url
        self.driver.get("file:///Users/caoqing/Desktop/COMP4350/apartment/bulletin/templates/bulletinBoard.html") #should be the url of bulletin board
        create = '//button[text()="New Bulletin"]'
        createButton = self.driver.find_element_by_xpath(create)
        createButton.click()
        self.driver.close()

    def test_create_new_bulletin(self):
        # url should be changed to create bulletin url
        self.driver.get("file:///Users/caoqing/Desktop/COMP4350/apartment/bulletin/templates/createBulletin.html")
        content = self.driver.find_element_by_name("Text1")
        content.send_keys("Attention! This is a test bulletin from selenium")
        create = '//button[text()="Create Bulletin"]'
        createButton = self.driver.find_element_by_xpath(create)
        createButton.click()
        self.driver.close()


    def test_add_comment(self):
        # url should be changed to bulletin url
        self.driver.get("file:///Users/caoqing/Desktop/COMP4350/apartment/bulletin/templates/bulletin.html")
        comment = self.driver.find_element_by_class_name("form-control")
        comment.send_keys("This is a test comment from selenium")
        add = '//button[text()="Add"]'
        addButton = self.driver.find_element_by_xpath(add)
        addButton.click()
        self.driver.close()

class ManagerSettingTestCase(unittest.TestCase):

    def setUp(self):
        """
        if your browser is chrome,change self.driver = webdriver.Firefox() to the follows
        chromedriver = "chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        """
        self.driver = webdriver.Firefox()

    def test_create_new_tenant(self):
        # the url should be changed to managerSetting url
        self.driver.get("file:///Users/caoqing/Desktop/COMP4350/apartment/apartmentApp/templates/managerSettings.html")
        name = self.driver.find_element_by_name("username")
        name.send_keys(Keys.CONTROL,'a')
        name.send_keys(Keys.DELETE)
        name.send_keys("qing")
        email = self.driver.find_element_by_name("email")
        email.send_keys(Keys.CONTROL,'a')
        email.send_keys(Keys.DELETE)
        email.send_keys("qing@gmail.com")
        psw = self.driver.find_element_by_name("password")
        psw.send_keys(Keys.CONTROL,'a')
        psw.send_keys(Keys.DELETE)
        psw.send_keys("123456")
        create = '//input[@type="submit" and @value="Create Tenant"]'
        createTenant = self.driver.find_element_by_xpath(create)
        createTenant.click()
        self.driver.close()

    def test_delete_tenant(self):
        # the url should be changed to managerSetting url
        self.driver.get("file:///Users/caoqing/Desktop/COMP4350/apartment/apartmentApp/templates/managerSettings.html")
        name = self.driver.find_element_by_name("username")
        name.send_keys(Keys.CONTROL,'a')
        name.send_keys(Keys.DELETE)
        name.send_keys("qing")
        remove = '//input[@type="submit" and @value="Remove Tenant"]'
        removeTenant = self.driver.find_element_by_xpath(remove)
        removeTenant.click()
        self.driver.close()

#run the tests
if __name__ == "__main__":
    unittest.main()

