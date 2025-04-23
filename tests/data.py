import random
import os



# класс содержит корректные данные зарегистрированного пользователя
class CorrectAuthorizationData:
    CORRECT_NAME = "rsv"
    CORRECT_EMAIL = "rsv19000@gmail.com"
    CORRECT_PASSWORD = "qwerty123"


# класс содержит НЕкорректные данные зарегистрированного пользователя
class IncorrectAuthorizationData:
    INCORRECT_PASSWORD = "123"


# класс содержит тест сообщений об ошибках
class ErrorMessages:
    TEXT_INCORRECT_PASSWORD = "Некорректный пароль"


# класс содержит информацию о кнопках
class Buttons:
    ORDER_BUTTON_TEXT = "Оформить заказ"


# генератор регистрационных данных
class GenerateRegistrationData:
    def __init__(self, base="sergeyrashchupkin", counter_file="counter.txt"):
        self.base = base
        self.counter_file = counter_file
        self.counter = self._load_counter()

# загрузка текущего значения счётчика из файла, если файл отсутствует — вернуть стартовое значение 15000
    def _load_counter(self):
        if os.path.exists(self.counter_file):
            with open(self.counter_file, "r") as f:
                return int(f.read())
        else:
            return 19150  # стартовое значение счётчика при первом запуске

# хранение текущего значения счётчика в файле, вызывается после генерации каждого набора данных
    def _save_counter(self):
        with open(self.counter_file, "w") as f:
            f.write(str(self.counter))

# енератор данных
    def generate_data(self):
        name = f"{self.base}{self.counter}"
        email = f"{name}@gmail.com"
        password = "pa" + ''.join(random.choices('0123456789!?', k=6)) + "ss"
        self.counter += 1
        self._save_counter()
        return {"name": name, "email": email, "password": password}




