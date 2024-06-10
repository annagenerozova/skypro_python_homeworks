from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.implicitly_wait(20)

driver.get("http://www.uitestingplayground.com/ajax")

blue_button_locator = "#ajaxButton"
driver.find_element(By.CSS_SELECTOR, blue_button_locator).click()

banner_locator = "#content > p"
banner = driver.find_element(By.CSS_SELECTOR, banner_locator)
text = banner.text

print(text)

driver.quit()