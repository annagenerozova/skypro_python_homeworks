from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(10)

modal_button_locator = '[class="modal-footer"]'
button= driver.find_element(By.CSS_SELECTOR, modal_button_locator).click()

sleep(5)
driver.quit()