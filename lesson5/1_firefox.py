from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for x in range (5):
    button_locator = '[onclick="addElement()"]'
    button= driver.find_element(By.CSS_SELECTOR, button_locator).click()
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print(len(delete_buttons))

sleep(15)
driver.quit()