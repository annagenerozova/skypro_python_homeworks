from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(3)

search_locator = '[type="number"]'
search_input= driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("1000")
sleep(3)
search_input.clear()
sleep(3)
search_input.send_keys("999")

sleep(5)