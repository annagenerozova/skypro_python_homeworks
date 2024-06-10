from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get(" http://uitestingplayground.com/dynamicid")

for x in range (3):
    button_locator = '[class="btn btn-primary"]'
    button= driver.find_element(By.CSS_SELECTOR, button_locator).click()

sleep(10)

driver.quit()

