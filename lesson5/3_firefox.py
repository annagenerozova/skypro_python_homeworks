from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")
for x in range (3):
    blue_button_locator = 'button.btn-primary'
    button= driver.find_element(By.CSS_SELECTOR, blue_button_locator).click()
    sleep(3)

sleep(10)
driver.quit()