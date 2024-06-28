from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_calculator(chrome_browser):
    chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    chrome_browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    chrome_browser.maximize_window()
    delay_input = chrome_browser.find_element(By.CSS_SELECTOR, '#delay')
    delay_input.clear()
    delay_input.send_keys("45")

    chrome_browser.find_element(By.XPATH, '//span[text()="7"]').click()
    chrome_browser.find_element(By.XPATH, '//span[text()="+"]').click()
    chrome_browser.find_element(By.XPATH, '//span[text()="8"]').click()
    chrome_browser.find_element(By.XPATH, '//span[text()="="]').click()
    
    WebDriverWait(chrome_browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = chrome_browser.find_element(By.CLASS_NAME , "screen").text
    #assert 'screen' in chrome_browser.find_element(By.ID , '//span[text()="15"]').get_attribute("class")

    assert result_text == "15"
 
