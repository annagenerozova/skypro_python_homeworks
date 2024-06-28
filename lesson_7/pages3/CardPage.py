from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CardPage:

    def __init__(self, browser):
        self.driver = browser
            
    def product (self):
        waiter = WebDriverWait(self.driver, 10)
        button_1 = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'))).click()
        button_2 = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'))).click()
        button_3 = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'))).click()
        button_basket = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.shopping_cart_link'))).click() 
        button_checkout = waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkout'))).click()
        

    