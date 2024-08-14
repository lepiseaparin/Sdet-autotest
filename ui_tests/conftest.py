import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Фикстура pytest с областью действия "session", которая устанавливает драйвер браузера
@pytest.fixture(scope="session")
def browser():
    # Устанавливаем и настраиваем драйвер Chrome с помощью ChromeDriverManager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # Максимизируем окно браузера, чтобы тесты проходили в полноэкранном режиме
    driver.maximize_window()
    # Команда yield возвращает драйвер браузера, чтобы его можно было использовать в тестах
    # после чего выполнение кода продолжится, когда тесты завершатся
    yield driver
    # Закрываем браузер после завершения всех тестов, чтобы очистить ресурсы
    driver.quit()
