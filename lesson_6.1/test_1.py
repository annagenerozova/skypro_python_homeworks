from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_form_submission():
    chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    chrome_browser.maximize_window()
    chrome_browser.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
    chrome_browser.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
    chrome_browser.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
    chrome_browser.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
    chrome_browser.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
    
    zip_code_locator = '[name="zip-code"]'
    zip_code_input = chrome_browser.find_element(By.CSS_SELECTOR, zip_code_locator)
    zip_code_input.clear()

    chrome_browser.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
    chrome_browser.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
    chrome_browser.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
    chrome_browser.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")

    chrome_browser.find_element(By.CSS_SELECTOR, "button").click()

    sleep (5)

    assert 'danger' in chrome_browser.find_element(By.ID , "zip-code").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "first-name").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "last-name").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID , "address").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID , "e-mail").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "phone").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "city").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "country").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID , "job-position").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "company").get_attribute("class")
