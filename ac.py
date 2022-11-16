from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def mouse_hover():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(30) #implicit wait is a flexible wait
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    myactions = ActionChains(driver)
    electronics_dropdown = driver.find_element(By.XPATH, "//div[text()='Electronics']")
    audio_drop_down = driver.find_element(By.XPATH, "//a[text()='Audio']")
    myactions.move_to_element(electronics_dropdown).pause(2).move_to_element(audio_drop_down).perform()
    time.sleep(30) #it is a hard wait

def drag_drop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(30)  # implicit wait is a flexible wait
    driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
    driver.maximize_window()
    myactions = ActionChains(driver)
    oslo_draggable_element = driver.find_element(By.XPATH, "//div[text()='Oslo' and contains(@id, 'box')]")
    norway_target_element = driver.find_element(By.XPATH, "//div[text()='Norway']")
    myactions.drag_and_drop(target=norway_target_element, source=oslo_draggable_element).perform()
    time.sleep(30)

def ctrl_select():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(30)  # implicit wait is a flexible wait
    driver.get("https://jqueryui.com/selectable/")
    driver.maximize_window()
    #frame_locator = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
    driver.switch_to.frame(0)
    item1_locator = driver.find_element(By.XPATH, "//li[text()='Item 1']")
    item2_locator = driver.find_element(By.XPATH, "//li[text()='Item 2']")
    item3_locator = driver.find_element(By.XPATH, "//li[text()='Item 3']")
    myactions = ActionChains(driver)
    myactions.key_down(Keys.CONTROL)
    myactions.click(item1_locator).click(item2_locator).click(item3_locator).perform()
    time.sleep(30)

drag_drop()