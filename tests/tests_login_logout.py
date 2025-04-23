from conftest import *
from locators import TestLocators
from data import *
from urls import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class TestLogin:

# проверка входа по кнопке "Войти в аккаунт" на главной странице
    def test_login_account_from_main_page_by_button_login_account(self, driver, open_page, login_registered_user):
        # открытие сайта - главная страница
        open_page(Urls.URL_MAIN_PAGE)
        # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT_MAIN_PAGE_LOCATOR).click()
        # вход зарегистрированного пользователя
        login_registered_user(CorrectAuthorizationData.CORRECT_EMAIL, CorrectAuthorizationData.CORRECT_PASSWORD)
        # текущий email зарегистрированного пользователя из атрибута "value"
        actual_email = driver.find_element(*TestLocators.EMAIL_PERSONAL_ACCOUNT_PAGE_LOCATOR).get_attribute('value')
        # сравнение текущего email с ожидаемым
        assert actual_email == CorrectAuthorizationData.CORRECT_EMAIL


# проверка входа по кнопке "Личный кабинет" на главной странице
    def test_login_account_from_main_page_by_button_personal_account(self, driver, open_page, login_registered_user):
        # открытие сайта - раздел "Регистрация"
        open_page(Urls.URL_MAIN_PAGE)
        # нажать ссылку "Личный кабинет" в хедере
        driver.find_element(*TestLocators.PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR).click()
        # вход зарегистрированного пользователя
        login_registered_user(CorrectAuthorizationData.CORRECT_EMAIL, CorrectAuthorizationData.CORRECT_PASSWORD)
        # текущий email зарегистрированного пользователя из атрибута "value"
        actual_email = driver.find_element(*TestLocators.EMAIL_PERSONAL_ACCOUNT_PAGE_LOCATOR).get_attribute('value')
        # сравнение текущего email с ожидаемым
        assert actual_email == CorrectAuthorizationData.CORRECT_EMAIL


# проверка входа по кнопке "Войти" в форме регистрации
    def test_login_account_from_registration_page_by_button_login_account(self, driver, open_page, login_registered_user):
        # открытие сайта - раздел "Регистрация"
        open_page(Urls.URL_REGISTRATION_PAGE)
        # нажать ссылку "Войти"
        driver.find_element(*TestLocators.LINK_LOGIN_ACCOUNT_REGISTRATION_PAGE_LOCATOR).click()
        # вход зарегистрированного пользователя
        login_registered_user(CorrectAuthorizationData.CORRECT_EMAIL, CorrectAuthorizationData.CORRECT_PASSWORD)
        # текущий email зарегистрированного пользователя из атрибута "value"
        actual_email = driver.find_element(*TestLocators.EMAIL_PERSONAL_ACCOUNT_PAGE_LOCATOR).get_attribute('value')
        # сравнение текущего email с ожидаемым
        assert actual_email == CorrectAuthorizationData.CORRECT_EMAIL


# проверка входа по кнопке "Войти" в форме восстановления пароля
    def test_login_account_from_forgot_password_page_by_button_login_account(self, driver, open_page, login_registered_user):
        # открытие сайта - раздел "Восстановление пароля"
        open_page(Urls.URL_FORGOT_PASSWORD)
        # нажать ссылку "Войти"
        driver.find_element(*TestLocators.LINK_LOGIN_ACCOUNT_FORGOT_PASSWORD_PAGE_LOCATOR).click()
        # вход зарегистрированного пользователя
        login_registered_user(CorrectAuthorizationData.CORRECT_EMAIL, CorrectAuthorizationData.CORRECT_PASSWORD)
        # текущий email зарегистрированного пользователя из атрибута "value"
        actual_email = driver.find_element(*TestLocators.EMAIL_PERSONAL_ACCOUNT_PAGE_LOCATOR).get_attribute('value')
        # сравнение текущего email с ожидаемым
        assert actual_email == CorrectAuthorizationData.CORRECT_EMAIL


# проверка выход по кнопке «Выйти» в личном кабинете
    def test_logout_from_account(self, driver, open_page, login_registered_user):
        # открытие сайта - главная страница
        open_page(Urls.URL_MAIN_PAGE)
        # нажать кнопку "Войти в аккаунт"
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT_MAIN_PAGE_LOCATOR).click()
        # вход зарегистрированного пользователя
        login_registered_user(CorrectAuthorizationData.CORRECT_EMAIL, CorrectAuthorizationData.CORRECT_PASSWORD)
        # нажать кнопку "Выход" в "Личном кабинете"
        driver.find_element(*TestLocators.BUTTON_EXIT_ACCOUNT_PAGE_LOCATOR).click()
        # ожидание, переход на страницу "Войти"
        WebDriverWait(driver, 5).until(EC.url_changes(Urls.URL_LOGIN_PAGE))
        # клик по ссылке "Личный кабинет" в хедере
        driver.find_element(*TestLocators.PARAGRAPH_PERSONAL_ACCOUNT_HEADER_LOCATOR).click()
        # текущий url не соответствует url личного кабинета
        assert Urls.URL_PERSONAL_ACCOUNT not in driver.current_url




