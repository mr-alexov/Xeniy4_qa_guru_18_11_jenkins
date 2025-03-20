from HW_way_1.pages.registration_page import RegistrationPage


def test_form(browser_manager):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name('Kseniya')
    registration_page.fill_last_name('Goryaeva')
    registration_page.email('Goryaeva@mail.ru')
    registration_page.gender()
    registration_page.mobile('8910123456')
    registration_page.dateOfBirth('November', '11', '1995')
    registration_page.subject('hist')
    registration_page.hobbies()
    registration_page.picture('pic.png')
    registration_page.currentAddress('Нижний Новгород')
    registration_page.scroll()
    registration_page.state()
    registration_page.city()
    registration_page.submit()

    registration_page.finish_form()
