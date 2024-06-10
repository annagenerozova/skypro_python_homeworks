from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")
waiter = WebDriverWait(driver, 40)

search_locator = '#newButtonName'
waiter.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, search_locator),))
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.clear()
search_input.send_keys("SkyPro")

button_locator = '#updatingButton'
driver.find_element(By.CSS_SELECTOR , button_locator).click()

waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, button_locator), "SkyPro"))

text_button = driver.find_element(By.CSS_SELECTOR , button_locator).text

print(text_button)

driver.quit()

