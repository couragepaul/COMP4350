import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

baseURL = "http://apartment-app.pfsa2harbh.us-west-2.elasticbeanstalk.com/"

def loginSession(self):
    #make sure we are in the home page -- uncomment if you want localhost testing
    # self.driver.get("http://127.0.0.1:8000/apartmentApp/")
    self.driver.get(baseURL)
    username = "COMP4350_SU"
    password = "COMP4350_PW"
    #username
    name = self.driver.find_element_by_id("username")
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


class ApartmentLoginTestCase(unittest.TestCase):
    """Test Case for logging into the app"""

    def setUp(self):
        # if your browser is chrome,change self.driver = webdriver.Firefox() to the follows
        #chromedriver = "chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        #self.driver = webdriver.Chrome(chromedriver)
        self.driver = webdriver.Firefox()

    def test_login(self):
        loginSession(self)

    def test_logout(self):
        logoutButton = self.driver.find_element_by_link_text("Log Out")
        logoutButton.click()

    def tearDown(self):
        self.driver.close()

class ApartmentSendMessageTestCase(unittest.TestCase):
    """Test Case for sending messages to a test user"""
    def setUp(self):
        # if your browser is chrome,change self.driver = webdriver.Firefox() to the follows
        #chromedriver = "chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        #self.driver = webdriver.Chrome(chromedriver)
        self.driver = webdriver.Firefox()
        loginSession(self)

    def test_sending_messages(self):
        #make sure we are in the home page
        # the url should be changed to create message url
        # self.driver.get("http://127.0.0.1:8000/apartmentApp/createMessageView")
        self.driver.get(baseURL + "/createMessageView")
        username = "COMP4350_SU"
        msg = "test message from selenium"
        urg = "1"
        #username
        name = self.driver.find_element_by_name("username")
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

    def tearDown(self):
        self.driver.close()



class ApartmentBulletinBoardTestCase(unittest.TestCase):

    def setUp(self):
        # if your browser is chrome,change self.driver = webdriver.Firefox() to the follows
        #chromedriver = "chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        #self.driver = webdriver.Chrome(chromedriver)
        self.driver = webdriver.Firefox()
        loginSession(self)

    def test_jump_from_bulletin_board_to_create_new_bulletin_page(self):
        # url should be changed to bulletin board url
        # self.driver.get("http://127.0.0.1:8000/apartmentApp/bulletinBoard")
        self.driver.get(baseURL + "/bulletinBoard")
        create = '//button[text()="New Bulletin"]'
        createButton = self.driver.find_element_by_xpath(create)
        createButton.click()

    def test_create_new_bulletin(self):
        # url should be changed to create bulletin url
        # self.driver.get("http://127.0.0.1:8000/apartmentApp/bulletinBoard/createBulletin")
        self.driver.get(baseURL + "/bulletinBoard/createBulletin")
        subject = self.driver.find_element_by_name("subject")
        subject.send_keys("Testing")
        content = self.driver.find_element_by_name("message")
        content.send_keys("Attention! This is a test bulletin from selenium")
        create = '//button[text()="Create Bulletin"]'
        createButton = self.driver.find_element_by_xpath(create)
        createButton.click()

    def test_add_comment(self):
        # url should be changed to bulletin url
        # need to double check this test TODO: fix test to work with proper bulletins
        # self.driver.get("http://127.0.0.1:8000/apartmentApp/bulletinBoard/10")
        self.driver.get(baseURL + "/bulletinBoard/1")
        comment = self.driver.find_element_by_name("message")
        comment.send_keys("This is a test comment from selenium")
        add = '//button[text()="Add"]'
        addButton = self.driver.find_element_by_xpath(add)
        addButton.click()

    def tearDown(self):
        self.driver.close()

class ManagerSettingTestCase(unittest.TestCase):

    def setUp(self):
        # if your browser is chrome,change self.driver = webdriver.Firefox() to the follows
        #chromedriver = "chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        #self.driver = webdriver.Chrome(chromedriver)
        self.driver = webdriver.Firefox()
        loginSession(self)

    def test_create_new_tenant(self):
        # the url should be changed to managerSetting url
        # self.driver.get("http://127.0.0.1:8000/apartmentApp/managerSettings")
        self.driver.get(baseURL + "/managerSettings")
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

    def test_delete_tenant(self):
        # the url should be changed to managerSetting url
        # self.driver.get("http://127.0.0.1:8000/apartmentApp/managerSettings")
        self.driver.get(baseURL + "/managerSettings")
        #TODO: Change this to be proper name, asked nick to change it
        name = self.driver.find_element_by_name("deleteUsername")
        name.send_keys(Keys.CONTROL,'a')
        name.send_keys(Keys.DELETE)
        name.send_keys("qing")
        remove = '//input[@type="submit" and @value="Remove Tenant"]'
        removeTenant = self.driver.find_element_by_xpath(remove)
        removeTenant.click()

    def tearDown(self):
        self.driver.close()

#run the tests
if __name__ == "__main__":
    unittest.main()

class ApartmentCalendarTestCase(unittest.TestCase):
    def setUp(self):
        # if your browser is chrome,change self.driver = webdriver.Firefox() to the follows
        #chromedriver = "chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        #self.driver = webdriver.Chrome(chromedriver)
        self.driver = webdriver.Firefox()
        loginSession(self)

    def test_create_an_event(self):
        self.driver.get(baseURL +"/calendar")
        createEventButton = self.driver.find_element_by_id("new-event-button")
        createEventButton.click()
        setEvent = self.driver.find_element_by_name("title")
        setEvent.send_keys("tests1")
        setLocation = self.driver.find_element_by_name("location")
        setLocation.send_keys("UC")
        setStartTime = self.driver.find_element_by_name("starttime")
        # fill date with 03/18/2016
        setStartTime.send_keys("03182016")
        #press tab to shift focus on time
        setStartTime.send_keys(Keys.TAB)
        #fill time with 02:00pm
        setStartTime.send_keys("0200PM")
        setEndTime = self.driver.find_element_by_name("endtime")
        setEndTime.send_keys("03242016")
        setEndTime.send_keys(Keys.TAB)
        setEndTime.send_keys("1100AM")
        setNotes = self.driver.find_element_by_name("message")
        setNotes.send_keys("testTestTest from notes")
        saveButton = self.driver.find_element_by_id("saveEventButton")
        saveButton.click()

    def test_create_event_no_end_time(self):
        self.driver.get(baseURL+"/calendar")
        createEventButton = self.driver.find_element_by_id("new-event-button")
        createEventButton.click()
        setEvent = self.driver.find_element_by_name("title")
        setEvent.send_keys("tests1")
        setLocation = self.driver.find_element_by_name("location")
        setLocation.send_keys("UC")
        setStartTime = self.driver.find_element_by_name("starttime")
        # fill date with 03/18/2016
        setStartTime.send_keys("03182016")
        #press tab to shift focus on time
        setStartTime.send_keys(Keys.TAB)
        #fill time with 02:00pm
        setStartTime.send_keys("0200PM")
        setNotes = self.driver.find_element_by_name("message")
        setNotes.send_keys("testTestTest from notes")
        saveButton = self.driver.find_element_by_id("saveEventButton")
        saveButton.click()

    def test_create_event_no_title(self):
        self.driver.get(baseURL +"/calendar")
        createEventButton = self.driver.find_element_by_id("new-event-button")
        createEventButton.click()
        setLocation = self.driver.find_element_by_name("location")
        setLocation.send_keys("UC")
        setStartTime = self.driver.find_element_by_name("starttime")
        # fill date with 03/18/2016
        setStartTime.send_keys("03182016")
        #press tab to shift focus on time
        setStartTime.send_keys(Keys.TAB)
        #fill time with 02:00pm
        setStartTime.send_keys("0200PM")
        setEndTime = self.driver.find_element_by_name("endtime")
        setEndTime.send_keys("03242016")
        setEndTime.send_keys(Keys.TAB)
        setEndTime.send_keys("1100AM")
        setNotes = self.driver.find_element_by_name("message")
        setNotes.send_keys("testTestTest from notes")
        saveButton = self.driver.find_element_by_id("saveEventButton")
        saveButton.click()

    def test_create_event_no_location(self):
        self.driver.get(baseURL +"/calendar")
        createEventButton = self.driver.find_element_by_id("new-event-button")
        createEventButton.click()
        setEvent = self.driver.find_element_by_name("title")
        setEvent.send_keys("tests1")
        setStartTime = self.driver.find_element_by_name("starttime")
        # fill date with 03/18/2016
        setStartTime.send_keys("03182016")
        #press tab to shift focus on time
        setStartTime.send_keys(Keys.TAB)
        #fill time with 02:00pm
        setStartTime.send_keys("0200PM")
        setEndTime = self.driver.find_element_by_name("endtime")
        setEndTime.send_keys("03242016")
        setEndTime.send_keys(Keys.TAB)
        setEndTime.send_keys("1100AM")
        setNotes = self.driver.find_element_by_name("message")
        setNotes.send_keys("testTestTest from notes")
        saveButton = self.driver.find_element_by_id("saveEventButton")
        saveButton.click()


    def test_jump_from_home_page_to_calendar(self):
        self.driver.get(baseURL + "/home")
        calendarButton = self.driver.find_element_by_link_text("Calendar")
        calendarButton.click()

    def test_jump_from_calendar_to_bulletin_page(self):
        self.driver.get(baseURL + "/calendar")
        bulletinButton = self.driver.find_element_by_link_text("Bulletin")
        bulletinButton.click()

    def test_click_prev_button_to_last_month(self):
        self.driver.get(baseURL + "/calendar")
        prevButton = self.driver.find_element_by_link_text("Prev")
        prevButton.click()

    def test_find_a_specific_month_year_from_menus(self):
        self.driver.get(baseURL + "/calendar")
        monthButton = self.driver.find_element_by_class_name("ui-datepicker-month")
        monthButton.click()
        # select a month by clicking arrow
        monthButton.send_keys(Keys.ARROW_DOWN);
        monthButton.send_keys(Keys.ARROW_DOWN);
        monthButton.send_keys(Keys.ARROW_DOWN);
        yearButton = self.driver.find_element_by_class_name("ui-datepicker-year")
        yearButton.click()
        # select a specific year
        monthButton.send_keys(Keys.ARROW_DOWN);
        monthButton.send_keys(Keys.ARROW_DOWN);
        monthButton.send_keys(Keys.ARROW_DOWN);
        monthButton.send_keys(Keys.ARROW_DOWN);
        monthButton.send_keys(Keys.ARROW_DOWN);

    def test_view_event(self):
        self.driver.get(baseURL + "/calendar")
        specificDate = self.driver.find_element_by_link_text("2")
        specificDate.click()
