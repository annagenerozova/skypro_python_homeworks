from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
    
    def delay(self):
        delay_input = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_input.clear()
        delay_input.send_keys("45")

    def calculator(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()

    def result(self):
        WebDriverWait(self._driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        result_text = self._driver.find_element(By.CLASS_NAME , "screen").text

        assert result_text == "15"
