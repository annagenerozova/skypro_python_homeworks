from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get(" http://uitestingplayground.com/dynamicid")

for x in range (3):
    button_locator = '[class="btn btn-primary"]'
    button= driver.find_element(By.CSS_SELECTOR, button_locator).click()

sleep(5)

