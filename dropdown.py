from selenium import webdriver
#from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
drop_down = Select(driver.find_element(By.XPATH, "//select[@id='RESULT_RadioButton-9']"))
drop_down.select_by_visible_text("Morning")
time.sleep(30)

