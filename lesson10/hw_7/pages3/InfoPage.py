from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class InfoPage:
    def __init__(self, browser):
        self.driver = browser

    @allure.step("Информация о доставке")
    def name (self):
        first_name_input= self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Анна")
        last_name_input= self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Генерозова")
        zip_input= self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("190011")
        button= self.driver.find_element(By.CSS_SELECTOR, '#continue').click()
        
