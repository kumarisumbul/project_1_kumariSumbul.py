from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH, "//button[text()='    click   ']").click()

list_of_windows = driver.window_handles#returns list of windows

for window in list_of_windows:
    '''driver.switch_to.window(window)
    print(window)
    print(driver.title)'''
    if(driver.title == "Frames & windows"):
        driver.switch_to.window(window)
        break

time.sleep(10)
driver.find_element(By.XPATH, "//a[text()='WebTable']").click()
time.sleep(10)


#singleton class