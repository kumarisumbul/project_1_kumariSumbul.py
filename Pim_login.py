import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService


def launch_browser2():
    driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(15)
    driver.find_element(By.XPATH, "//div/input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//div/input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//div/button[@type='submit']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[text()='PIM']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()=' Add ']").click()
    driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()
    driver.find_element(By.XPATH, "//div/input[@name='firstName']").send_keys("x")
    driver.find_element(By.XPATH, "//div/input[@name='middleName']").send_keys("y")
    driver.find_element(By.XPATH, "//div/input[@name='lastName']").send_keys("z")
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
    return driver

mydriver = launch_browser2()