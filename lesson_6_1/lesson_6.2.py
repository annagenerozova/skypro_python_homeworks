from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

delay_locator = '#delay'
delay_input= driver.find_element(By.CSS_SELECTOR, delay_locator)
delay_input.clear()
delay_input.send_keys("45")

waiter = WebDriverWait(driver, 10)
button_7 = waiter.until(EC.presence_of_element_located((By.XPATH, '//span[text()="7"]')))
button_7.click()

button_plus = waiter.until(EC.presence_of_element_located((By.XPATH, '//span[text()="+"]')))
button_plus.click()

button_8 = waiter.until(EC.presence_of_element_located((By.XPATH, '//span[text()="8"]')))
button_8.click()

button_equally = waiter.until(EC.presence_of_element_located((By.XPATH, '//span[text()="="]')))
button_equally.click()


result_waiter = WebDriverWait(driver, 45)
result = result_waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

assert result, "Expected result '15' not found"
print("Test passed: Result is 15")
 
driver.quit()