import allure

from HW_way_1.pages.registration_page import RegistrationPage


def test_form(browser_manager):
    registration_page = RegistrationPage()

    with allure.step('Открываем главную страницу'):
        registration_page.open()

    with allure.step('Заполняем поле First Name'):
        registration_page.fill_first_name('Kseniya')
    with allure.step('Заполняем поле Last name'):
        registration_page.fill_last_name('Goryaeva')
    with allure.step('Заполняем поле email'):
        registration_page.email('Goryaeva@mail.ru')
    with allure.step('Заполняем поле Gender'):
        registration_page.gender('Female')
    with allure.step('Заполняем поле Mobile'):
        registration_page.mobile('8910123456')
    with allure.step('Заполняем поле Date of Birth'):
        registration_page.dateOfBirth('November', '11', '1995')
    with allure.step('Заполняем поле Subjects'):
        registration_page.subject('hist')
    with allure.step('Заполняем поле Hobbies'):
        registration_page.hobbies('Sports')
    with allure.step('Заполняем поле Picture'):
        registration_page.picture('pic.png')
    with allure.step('Заполняем поле CurrentAddress'):
        registration_page.currentAddress('Нижний Новгород')
    with allure.step('Скролл вниз'):
        registration_page.scroll()
    with allure.step('Заполняем поле State'):
        registration_page.state()
    with allure.step('Заполняем поле City'):
        registration_page.city()
    with allure.step('Нажимаем на кнопку Submit'):
        registration_page.submit()

    with allure.step('Проверка финального окна'):
        registration_page.finish_form()
