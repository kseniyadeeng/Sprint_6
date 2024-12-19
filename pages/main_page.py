import allure
import time
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать прогрузки кнопки "Заказать" в хэдере')
    def wait_visibility_of_order_button_header(self):
        self.wait_visibility_of_element(MainPageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Кликнуть по кнопке "Заказать" в хэдере')
    def click_on_order_button_header(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Подождать прогрузки логотипа "Самокат" в хэдере')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Подождать прогрузки логотипа "Яндекс" в хэдере')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.HEADER_YANDEX_LOGO)

    @allure.step('Кликнуть по логотипу "Самокат" в хэдере')
    def click_on_header_logo_scooter(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть по логотипу "Яндекс" в хэдере')
    def click_on_header_logo_yandex(self):
        self.click_to_element(MainPageLocators.HEADER_YANDEX_LOGO)

    @allure.step('Подождать прогрузки заголовка "Вопросы о важном"')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.IMPORTANT_QUESTIONS_HEADER)

    @allure.step('Проверить отображение заголовка "Вопросы о важном"')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.IMPORTANT_QUESTIONS_HEADER)

    @allure.step('Проскроллить до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step('Подождать прогрузки нужного номера вопроса в вкладке "Вопросы о важном"')
    def wait_visibility_of_faq_item(self, question_key):
        self.wait_visibility_of_element(MainPageLocators.FAQ_QUESTIONS[question_key])

    @allure.step('Кликнуть на нужный номер вопроса в вкладке "Вопросы о важном"')
    def click_on_faq_item(self, question_key):
        self.click_to_element(MainPageLocators.FAQ_QUESTIONS[question_key])

    @allure.step('Подождать прогрузки нужного номера ответа в вкладке "Вопросы о важном"')
    def wait_visibility_of_faq_answer(self, answer_key):
        self.wait_visibility_of_element(MainPageLocators.FAQ_ANSWERS[answer_key])

    @allure.step('Получить текст нужного номера ответа в вкладке "Вопросы о важном"')
    def get_displayed_text_from_faq_answer(self, answer_key):
        return self.get_text_from_element(MainPageLocators.FAQ_ANSWERS[answer_key])

    @allure.step('Подождать, пока заголовок страницы не станет заданным')
    def wait_for_title_to_be(self, title, timeout=10):
        """Ожидаем, пока заголовок страницы не станет равным заданному."""
        end_time = time.time() + timeout
        while time.time() < end_time:
            if self.get_page_title() == title:
                return True
            time.sleep(0.5)
        raise Exception(f'Заголовок страницы не стал "{title}" за {timeout} секунд.')
