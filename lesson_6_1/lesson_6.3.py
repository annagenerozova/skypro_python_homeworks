from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

usename_locator = '#user-name'
usename_input= driver.find_element(By.CSS_SELECTOR, usename_locator)
usename_input.send_keys("standard_user")

password_locator = '#password'
password_input= driver.find_element(By.CSS_SELECTOR, password_locator)
password_input.send_keys("secret_sauce")

button_login= driver.find_element(By.CSS_SELECTOR, '#login-button').click()

waiter = WebDriverWait(driver, 10)
button_1 = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'))).click()
button_2 = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'))).click()
button_3 = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'))).click()
button_basket = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.shopping_cart_link'))).click()
button_checkout = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout'))).click()

first_name_locator = '#first-name'
first_name_input= driver.find_element(By.CSS_SELECTOR, first_name_locator)
first_name_input.send_keys("Анна")

last_name_locator = '#last-name'
last_name_input= driver.find_element(By.CSS_SELECTOR, last_name_locator)
last_name_input.send_keys("Генерозова")

zip_locator = '#postal-code'
zip_input= driver.find_element(By.CSS_SELECTOR, zip_locator)
zip_input.send_keys("190011")


button= driver.find_element(By.CSS_SELECTOR, '#continue').click()

total = driver.find_element(By.CSS_SELECTOR, '[class="summary_total_label"]')
text = total.text

assert text == 'Total: $58.29', f"Expected total to be $58.29, but got {text}"
print("Test passed: Total is $58.29")

driver.quit()

