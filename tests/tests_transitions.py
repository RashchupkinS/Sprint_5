from conftest import *
from locators import *
from urls import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class TestTransitions:

# проверка перехода из личного кабинета по клику на «Конструктор»
    def test_transition_by_click_to_constructor_from_personal_account(self, driver, open_page, login_registered_user):
        # открытие сайта - главная страница
        open_page(Urls.URL_MAIN_PAGE)
        # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT_MAIN_PAGE_LOCATOR).click()
        # вход зарегистрированного пользователя
        login_registered_user(CorrectAuthorizationData.CORRECT_EMAIL, CorrectAuthorizationData.CORRECT_PASSWORD)
        # нажать ссылку "Конструктор"
        driver.find_element(*TestLocators.PARAGRAPH_CONSTRUCTOR_HEADER_LOCATOR).click()
        # ожидание, проверка загрузки страницы и видимость кнопки "Оформить заказ"
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR)
        )
        order_button = driver.find_element(*TestLocators.BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR)
        # сравнение текста кнопки "Оформить заказ"
        assert order_button.text == Buttons.ORDER_BUTTON_TEXT


# проверка перехода из личного кабинета по клику на логотип Stellar Burgers
    def test_transition_by_click_to_stellar_burger_from_personal_account(self, driver, open_page, login_registered_user):
        # открытие сайта - главная страница
        open_page(Urls.URL_MAIN_PAGE)
        # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT_MAIN_PAGE_LOCATOR).click()
        # вход зарегистрированного пользователя
        login_registered_user(CorrectAuthorizationData.CORRECT_EMAIL, CorrectAuthorizationData.CORRECT_PASSWORD)
        # нажать логотип "Stellar Burgers"
        driver.find_element(*TestLocators.LOGO_STELLAR_BURGERS_HEADER_LOCATOR).click()
        # ожидание, проверка загрузки страницы и видимость кнопки "Оформить заказ"
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(TestLocators.BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR)
        )
        order_button = driver.find_element(*TestLocators.BUTTON_PLACE_ORDER_CONSTRUCTOR_PAGE_LOCATOR)
        # сравнение текста кнопки "Оформить заказ"
        assert order_button.text == Buttons.ORDER_BUTTON_TEXT


# проверка перехода по клику на «Личный кабинет», пользователь НЕ авторизован
    def test_transition_by_click_to_personal_account_unauthorized_user(self, driver, open_page):
        # открытие сайта - главная страница
        open_page(Urls.URL_MAIN_PAGE)
        # нажать кнопку "Личный кабинет"
        driver.find_element(*TestLocators.PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR).click()
        # текущий url не соответствует url личного кабинета
        assert Urls.URL_PERSONAL_ACCOUNT not in driver.current_url


# проверка перехода по клику на «Личный кабинет», пользователь авторизован
    def test_transition_by_click_to_personal_account_authorized_user(self, driver, open_page, login_registered_user):
        # открытие сайта - главная страница
        open_page(Urls.URL_MAIN_PAGE)
        # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT_MAIN_PAGE_LOCATOR).click()
        # вход зарегистрированного пользователя
        login_registered_user(CorrectAuthorizationData.CORRECT_EMAIL, CorrectAuthorizationData.CORRECT_PASSWORD)
        # нажать кнопку "Личный кабинет"
        driver.find_element(*TestLocators.PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR).click()
        # текущий url соответствует url личного кабинета
        assert driver.current_url == Urls.URL_PERSONAL_ACCOUNT




