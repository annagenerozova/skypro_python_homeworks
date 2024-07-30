from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class ResultPage:
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Сравнение ФР с ОР")
    def result (self):
        total = self.driver.find_element(By.CSS_SELECTOR, '[class="summary_total_label"]')
        text = total.text

        assert text == 'Total: $58.29', f"Expected total to be $58.29, but got {text}"
        print("Test passed: Total is $58.29")