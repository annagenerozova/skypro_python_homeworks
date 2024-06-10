from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range (5):
    button_locator = '[onclick="addElement()"]'
    button= driver.find_element(By.CSS_SELECTOR, button_locator).click()
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print(len(delete_buttons))

sleep(5)

