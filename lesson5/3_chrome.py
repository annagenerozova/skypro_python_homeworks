from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")
for x in range (3):
    blue_button_locator = 'button.btn-primary'
    button= driver.find_element(By.CSS_SELECTOR, blue_button_locator).click()
    trigger_button_locator = 'alert("Primary button pressed")' # Локатор кнопки, вызывающей alert
    driver.find_element(By.CSS_SELECTOR, trigger_button_locator).click()

sleep(10)