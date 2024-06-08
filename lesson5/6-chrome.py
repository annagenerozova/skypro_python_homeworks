from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get(" http://the-internet.herokuapp.com/login")
sleep(3)

username_locator = '[id="username"]'
username_input= driver.find_element(By.CSS_SELECTOR, username_locator)
username_input.send_keys("tomsmith")

password_locator = '[id="password"]'
password_input= driver.find_element(By.CSS_SELECTOR, password_locator)
password_input.send_keys("SuperSecretPassword!")

button_locator = '[class="radius"]'
button= driver.find_element(By.CSS_SELECTOR, button_locator).click()

sleep(5)