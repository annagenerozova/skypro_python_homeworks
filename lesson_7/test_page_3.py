from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages3.RegistrationPage import RegistrationPage
from pages3.CardPage import CardPage
from pages3.InfoPage import InfoPage
from pages3.ResultPage import ResultPage

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













