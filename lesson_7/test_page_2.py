from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages2.MainPage import MainPage

def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) #Переменная хранит экземпляр класса MainPage
   
    main_page.delay()
    main_page.calculator()
    main_page.result()

    browser.quit()
    
 
