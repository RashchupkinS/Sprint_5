from locators import *
from data import *
from urls import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class TestRegistrationPage:

# проверка успешной регистрации при вводе валидных значений, данные регистрации генерируются автоматически
    def test_successful_registration_input_correct_data(self, driver, open_page, registration_data, login_registered_user):
        # переменные хранящие текущие регистрационные данные теста
        current_test_name = registration_data["name"]
        current_test_email = registration_data["email"]
        current_test_password = registration_data["password"]
        # открытие сайта - раздел "Регистрация"
        open_page(Urls.URL_REGISTRATION_PAGE)
        # заполнение поля "Имя"
        driver.find_element(*TestLocators.INPUT_NAME_LOCATOR).send_keys(current_test_name)
        # заполнение поля "Email"
        driver.find_element(*TestLocators.INPUT_EMAIL_LOCATOR).send_keys(current_test_email)
        # заполнение поля "Пароль"
        driver.find_element(*TestLocators.INPUT_PASSWORD_LOCATOR).send_keys(current_test_password)
        # нажать кнопку "Зарегистрироваться"
        driver.find_element(*TestLocators.BUTTON_REGISTRATION_LOCATOR).click()
        # ожидание, проверка перехода к форме "Вход" и видимости кнопки "Войти"
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_LOCATOR))
        # заполнение данных для входа в аккаунт, данными сгенерированными для этого теста
        login_registered_user(current_test_email, current_test_password)
        # проверка, что текущая страница - страница личного кабинета
        assert driver.current_url == Urls.URL_PERSONAL_ACCOUNT_PAGE


# проверка вывода ошибки при вводе некорректного пароля при регистрации
    def test_error_incorrect_password_three_digit_password(self, driver, open_page, registration_data):
        # открытие сайта - раздел "Регистрация"
        open_page(Urls.URL_REGISTRATION_PAGE)
        # заполнение поля "Имя"
        driver.find_element(*TestLocators.INPUT_NAME_LOCATOR).send_keys(registration_data["name"])
        # заполнение поля "Email"
        driver.find_element(*TestLocators.INPUT_EMAIL_LOCATOR).send_keys(registration_data["email"])
        # заполнение поля "Пароль" некорректными данными
        driver.find_element(*TestLocators.INPUT_PASSWORD_LOCATOR).send_keys(IncorrectAuthorizationData.INCORRECT_PASSWORD)
        # нажать кнопку "Зарегистрироваться"
        driver.find_element(*TestLocators.BUTTON_REGISTRATION_LOCATOR).click()
        # ожидание появления текста "Некорректный пароль"
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(TestLocators.ERROR_INCORRECT_PASSWORD_LOCATOR)
        )
        incorrect_password = driver.find_element(*TestLocators.ERROR_INCORRECT_PASSWORD_LOCATOR)
        # равнение полученного текста с ожидаемым
        assert incorrect_password.text == ErrorMessages.TEXT_INCORRECT_PASSWORD




