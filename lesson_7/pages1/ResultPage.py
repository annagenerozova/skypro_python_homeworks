from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:
    def __init__(self, browser):
        self.driver = browser

    def color(self):
        assert 'danger' in self.driver.find_element(By.ID , "zip-code").get_attribute("class")
        assert "success" in self.driver.find_element(By.ID, "first-name").get_attribute("class")
        assert "success" in self.driver.find_element(By.ID, "last-name").get_attribute("class")
        assert "success" in self.driver.find_element(By.ID , "address").get_attribute("class")
        assert "success" in self.driver.find_element(By.ID , "e-mail").get_attribute("class")
        assert "success" in self.driver.find_element(By.ID, "phone").get_attribute("class")
        assert "success" in self.driver.find_element(By.ID, "city").get_attribute("class")
        assert "success" in self.driver.find_element(By.ID, "country").get_attribute("class")
        assert "success" in self.driver.find_element(By.ID , "job-position").get_attribute("class")
        assert "success" in self.driver.find_element(By.ID, "company").get_attribute("class")
