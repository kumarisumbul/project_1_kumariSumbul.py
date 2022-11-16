from selenium import webdriver
#from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#synchronisation
def implicit_wait():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.yatra.com/")
    driver.find_element(By.XATH, "//input[@value='Check Your Refund']").click()
    page_source = driver.page_source
    print(page_source)

def explicit_wait():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.yatra.com/")
    my_element = WebDriverWait(driver, 10).\
        until(expected_conditions.presence_of_element_located((By.XATH, "//input[@value='Check Your Refund']")))
    my_element.click()
    time.sleep(30)


explicit_wait()


