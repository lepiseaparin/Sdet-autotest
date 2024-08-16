from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page import BasePage


class RegistrationPage(BasePage):
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[@for='gender-radio-1']")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    MONTH_SELECT = (By.CLASS_NAME, "react-datepicker__month-select")
    YEAR_SELECT = (By.CLASS_NAME, "react-datepicker__year-select")
    DAY_SELECT = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month'))]")
    SUBJECTS = (By.ID, "subjectsInput")
    PICTURE = (By.ID, "uploadPicture")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "react-select-3-input")
    CITY = (By.ID, "react-select-4-input")
    SUBMIT = (By.ID, "submit")

    '''Методы заполнения и формы отправки данных'''
    def fill_first_name(self, name):
        self.find_element(self.FIRST_NAME).send_keys(name)

    def fill_last_name(self, name):
        self.find_element(self.LAST_NAME).send_keys(name)

    def fill_email(self, email):
        self.find_element(self.EMAIL).send_keys(email)

    def select_gender(self):
        self.find_element(self.GENDER_MALE).click()

    def fill_mobile(self, number):
        self.find_element(self.MOBILE).send_keys(number)

    def fill_date_of_birth(self, day, month, year):
        # Открываем календарь
        date_input = self.find_element(self.DATE_OF_BIRTH)
        date_input.click()

        # Выбираем месяц
        month_select = Select(self.find_element(self.MONTH_SELECT))
        month_select.select_by_value(str(month - 1))  # В селекторе месяцы начинаются с 0

        # Выбираем год
        year_select = Select(self.find_element(self.YEAR_SELECT))
        year_select.select_by_value(str(year))

        # Выбираем день
        day_select = self.driver.find_elements(*self.DAY_SELECT)
        for day_option in day_select:
            if day_option.text == str(day):
                day_option.click()
                break

        # Отправляем новую дату

    def fill_subjects(self, subject):
        subjects_input = self.find_element(self.SUBJECTS)
        subjects_input.send_keys(subject)
        subjects_input.send_keys("\n")

    def upload_picture(self, file_path):
        self.find_element(self.PICTURE).send_keys(file_path)

    def fill_current_address(self, address):
        self.find_element(self.CURRENT_ADDRESS).send_keys(address)

    def select_state(self, state):
        state_input = self.find_element(self.STATE)
        state_input.send_keys(state)
        state_input.send_keys("\n")

    def select_city(self, city):
        city_input = self.find_element(self.CITY)
        city_input.send_keys(city)
        city_input.send_keys("\n")

    def submit_form(self):
        self.find_element(self.SUBMIT).click()

