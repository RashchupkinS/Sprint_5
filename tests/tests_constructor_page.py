from locators import *
from urls import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class TestConstructorPage:

# проверка работы перехода к разделу "Булки"
    def test_transition_to_partition_bread(self, driver, open_page):
        # открытие сайта - раздел "Конструктор"
        open_page(Urls.URL_MAIN_PAGE)
        # клик раздел "Соусы"
        driver.find_element(*TestLocators.SAUCES_LOCATOR).click()
        # клик раздел "Булки"
        driver.find_element(*TestLocators.BREAD_LOCATOR).click()
        # проверка присутствия и видимости выбранного элемента в DOM
        current_element_is_visible = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.CURRENT_TAB_CONSTRUCTOR_LOCATOR)
        )
        assert current_element_is_visible


# проверка работы перехода к разделу "Соусы"
    def test_transition_to_partition_sauces(self, driver, open_page):
        # открытие сайта - раздел "Конструктор"
        open_page(Urls.URL_MAIN_PAGE)
        # клик раздел "Начинки"
        driver.find_element(*TestLocators.FILLINGS_LOCATOR).click()
        # клик раздел "Соусы"
        driver.find_element(*TestLocators.SAUCES_LOCATOR).click()
        # проверка присутствия и видимости выбранного элемента в DOM
        current_element_is_visible = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.CURRENT_TAB_CONSTRUCTOR_LOCATOR)
        )
        assert current_element_is_visible


# проверка работы перехода к разделу "Начинки"
    def test_transition_to_partition_fillings(self, driver, open_page):
        # открытие сайта - раздел "Конструктор"
        open_page(Urls.URL_MAIN_PAGE)
        # клик раздел "Соусы"
        driver.find_element(*TestLocators.SAUCES_LOCATOR).click()
        # клик раздел "Начинки"
        driver.find_element(*TestLocators.FILLINGS_LOCATOR).click()
        # проверка присутствия и видимости выбранного элемента в DOM
        current_element_is_visible = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(TestLocators.CURRENT_TAB_CONSTRUCTOR_LOCATOR)
        )
        assert current_element_is_visible




