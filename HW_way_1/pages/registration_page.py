import os

from selene import browser, have, command
from HW_way_1.HW_way_1 import resources


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        browser.config.timeout = 30

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def email(self, value):
        browser.element('#userEmail').type(value)

    def gender(self, value):
        # browser.element('#gender-radio-2').perform(command.js.click)
        # browser.element('#gender-radio-1 + .custom-control-label')
        browser.element(f'[name=gender][value={value}]').perform(command.js.click)


    def dateOfBirth(self, month, day, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def mobile(self, value):
        browser.element('#userNumber').type(value)

    def subject(self, value):
        browser.element('#subjectsInput').type(value)
        browser.element('#react-select-2-option-0').click()

    def hobbies(self,value):
        # browser.element('#hobbies-checkbox-1').perform(command.js.click)
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(value)).click()

    def picture(self,path):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(os.path.join(os.path.dirname(__file__), f"../resources/{path}")))

    def currentAddress(self, value):
        browser.element('#currentAddress').type(value)

    def scroll(self):
        browser.execute_script("window.scrollBy(0,6000)")

    def state(self):
        browser.element('#state .css-tlfecz-indicatorContainer').click()
        browser.element('#react-select-3-option-1').click()

    def city(self):
        browser.element('#city .css-tlfecz-indicatorContainer').click()
        browser.element('#react-select-4-option-2').click()

    def submit(self):
        browser.element('#submit').click()

    def finish_form(self):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                'Kseniya Goryaeva',
                'Goryaeva@mail.ru',
                'Female',
                '8910123456',
                '11 November,1995',
                'History',
                'Sports',
                'pic.png',
                'Нижний Новгород',
                'Uttar Pradesh Merrut'
            )
        )
