from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.volunteer_page_elements import VolunteerPageElements

driver = webdriver.Chrome()
vpc = VolunteerPageElements(driver)
def testCase1():
    driver.implicitly_wait(5)
    vpc.enterFirstName("abc")

def testCase2():
    vpc