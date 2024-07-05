from selene import browser, by, command, be, have
import allure
from guru_qahacking_tests.data.emails import Email
from guru_qahacking_tests.data.user import User


class MainPage:

    @allure.step('Открытие сайта')
    def open_browser(self):
        browser.open('')
        return self

    @allure.step('Переход на страницу "Подробнее о питомнике"')
    def check_open_details(self):
        browser.element('.uk-button-primary').click()
        browser.element(by.partial_text('Наши питомцы обладают хорошей и'))
        return self

    @allure.step('Переход на страницу "Магазин"')
    def check_open_shop(self):
        browser.element('.uk-navbar-nav').element('.uk-parent').click()
        browser.element(by.partial_text('Каталог товаров'))
        return self


class SubscriptionMainPage:

    def __init__(self):
        self.subscription_element_email = browser.element('.el-input')

    @allure.step('Ввод email')
    def fill_email(self, email: Email):
        self.subscription_element_email.perform(command.js.scroll_into_view)
        self.subscription_element_email.type(email)
        return self

    @allure.step('Отправка email')
    def send_email(self):
        browser.element('.uk-form-icon').click()
        return self

    @allure.step('Сообщение при успешной отправке e-mail')
    def success_email(self):
        browser.element('.message').should(have.text('Подписка оформлена'))
        return self

    @allure.step('Сообщение при отправке некорректного e-mail')
    def error_email(self):
        browser.element('.message').should(have.text('Введите корректный email'))
        return self


class QuestionMainPage:

    def __init__(self):
        self.question_element_name = browser.element('#mod-rscontact-full-name-91')
        self.question_element_send_button = browser.element('#mod-rscontact-submit-btn-91')

    @allure.step('Ввод имени')
    def fill_name(self, user: User):
        self.question_element_name.perform(command.js.scroll_into_view)
        self.question_element_name.type(user.name)
        return self

    @allure.step('Ввод email')
    def fill_mail(self, user: User):
        browser.element('#mod-rscontact-email-91').type(user.mail)
        return self

    @allure.step('Ввод номера телефона')
    def fill_phone(self, user: User):
        browser.element('#mod-rscontact-mobile-phone-91').type(user.phone)
        return self

    @allure.step('Ввод вопроса')
    def fill_question(self, user: User):
        browser.element('#mod-rscontact-subject-91').type(user.question)
        return self

    @allure.step('Отправка формы с вопросом')
    def send_form_question(self):
        self.question_element_send_button.perform(command.js.scroll_into_view)
        self.question_element_send_button.click()
        return self

    @allure.step('Проверка обязательного поля E-mail')
    def show_error(self):
        browser.element('#mod-rscontact-email-91-error').should(have.text('Please type your e-mail address.')).should(be.visible)