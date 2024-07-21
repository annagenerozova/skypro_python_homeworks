from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages3.RegistrationPage import RegistrationPage
from pages3.CardPage import CardPage
from pages3.InfoPage import InfoPage
from pages3.ResultPage import ResultPage
import allure

@allure.epic("Магазин") 
@allure.severity("blocker")
@allure.title("Работа с онлайн магазином")
@allure.description ("Регистрация, добавлние товара и работа с корзиной")
@allure.feature("Purchases")
def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    registration_page = RegistrationPage(browser)
    registration_page.field()

    card_page = CardPage(browser)
    card_page.product()

    info_page = InfoPage(browser)
    info_page.name()

    result_page = ResultPage(browser)
    result_page.result()

    browser.quit()













