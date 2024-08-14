import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui_tests.pages.registration_page import RegistrationPage
import os


def test_registration(browser):
    # Создание экземпляра RegistrationPage с браузером
    registration_page = RegistrationPage(browser)

    # Открытие страницы с формой регистрации
    registration_page.open("https://demoqa.com/automation-practice-form")

    # Заполнение формы
    registration_page.fill_first_name("John")
    registration_page.fill_last_name("Doe")
    registration_page.fill_email("john.doe@example.com")
    registration_page.select_gender()
    registration_page.fill_mobile("1234567890")
    registration_page.fill_date_of_birth(day=6, month=8, year=2001)
    registration_page.fill_subjects("Maths")

    # Получаем  путь к изображению
    file_path = os.path.join('C:/Users/jackp/kulas/Simbir-testovoe/ui_tests/images/test_image.jpg')

    # Диагностика: вывод пути и проверка существования файла
    print(f"Absolute path to the image: {file_path}")
    assert os.path.exists(file_path), f"File not found at {file_path}"

    registration_page.upload_picture(file_path)

    registration_page.fill_current_address("123 Test St")
    registration_page.select_state("NCR")
    registration_page.select_city("Delhi")
    registration_page.submit_form()

    # Ожидание появления модального окна
    wait = WebDriverWait(browser, 10)
    modal_title = wait.until(EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))).text
    assert modal_title == "Thanks for submitting the form"

    # Вывод всех значений из таблицы для диагностики
    modal_content = browser.find_element(By.CLASS_NAME, "modal-body").text
    print(modal_content)

    # Дополнительные проверки значений в модальном окне
    assert "John" in modal_content
    assert "Doe" in modal_content
    assert "john.doe@example.com" in modal_content
    assert "1234567890" in modal_content
    assert "Maths" in modal_content
    assert "123 Test St" in modal_content
    assert "NCR" in modal_content
    assert "Delhi" in modal_content

