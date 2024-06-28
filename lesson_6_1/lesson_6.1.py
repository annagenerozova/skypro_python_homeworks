from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name_locator = '[name="first-name"]'
first_name_input= driver.find_element(By.CSS_SELECTOR, first_name_locator)
first_name_input.send_keys("Иван")


last_name_locator = '[name="last-name"]'
last_name_input= driver.find_element(By.CSS_SELECTOR, last_name_locator)
last_name_input.send_keys("Петров")

address_locator = '[name="address"]'
address_input= driver.find_element(By.CSS_SELECTOR, address_locator)
address_input.send_keys("Ленина, 55-3")

email_locator = '[name="e-mail"]'
email_input= driver.find_element(By.CSS_SELECTOR, email_locator)
email_input.send_keys("test@skypro.com")

phone_locator = '[name="phone"]'
phone_input= driver.find_element(By.CSS_SELECTOR, phone_locator)
phone_input.send_keys("+7985899998787")

zip_code_locator = '[name="zip-code"]'
zip_code_input = driver.find_element(By.CSS_SELECTOR, zip_code_locator)
zip_code_input.clear()

city_locator = '[name="city"]'
city_input= driver.find_element(By.CSS_SELECTOR, city_locator)
city_input.send_keys("Москва")

country_locator = '[name="country"]'
country_input= driver.find_element(By.CSS_SELECTOR, country_locator)
country_input.send_keys("Россия")

job_locator = '[name="job-position"]'
job_input= driver.find_element(By.CSS_SELECTOR, job_locator)
job_input.send_keys("QA")

company_locator = '[name="company"]'
company_input= driver.find_element(By.CSS_SELECTOR, company_locator)
company_input.send_keys("SkyPro")

button= driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

waiter = WebDriverWait(driver, 20)
waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, zip_code_locator)))

# Проверка цвета фона поля Zip code
zip_code_classes = zip_code_input.get_attribute('class')
assert 'alert-danger' in zip_code_classes, "Zip code field is not highlighted red"

# Проверка цвета фона остальных полей
fields = [
    first_name_input,
    last_name_input,
    address_input,
    email_input,
    phone_input,
    city_input,
    country_input,
    job_input,
    company_input
]

for field in fields:
    field_classes = field.get_attribute('class')
    assert 'alert-success' in field_classes, f"Field {field.get_attribute('name')} is not highlighted green"

print("All assertions passed.")

driver.quit()