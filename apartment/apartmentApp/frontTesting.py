import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://127.0.0.1:8000/apartmentApp/")
name = driver.find_element_by_name("username")
# name.send_keys("jourey")
password = driver.find_element_by_name("password")
# password.send_keys("123123")
password.send_keys(Keys.RETURN)
# driver.close()