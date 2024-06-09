from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

for _ in range(3):
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    sleep(2)
    driver.switch_to.alert.accept()

sleep(3)

driver.quit()

