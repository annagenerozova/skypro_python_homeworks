from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages1.MainPage import MainPage
from pages1.ResultPage import ResultPage
import allure

@allure.epic("Форма заполнения") 
@allure.severity("blocker")
@allure.title("Работа с заполнением данных в поля")
@allure.description ("Проверка,правильного отображения цветов после заполнения поля")
@allure.feature("Registration")
def test_form_submission():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser) #Переменная хранит экземпляр класса MainPage
   
    main_page.field()

    result_page = ResultPage(browser)
    result_page.color()
    
    browser.quit()
   