import allure
from locators.order_locators import OrderFormLocators
from pages.home_page import HomePage


class OrderPage(HomePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Выбрать станцию метро из выпадающего списка')
    def select_station(self):
        self.click_to_element(OrderFormLocators.SELECT_ITEM_IN_DROPDOWN_METRO)

    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_entry_first_form(self, name, surname, address, metro_station, phone):
        self.wait_visibility_of_element(OrderFormLocators.NAME_INPUT)

        if self.send_keys_to_input(OrderFormLocators.NAME_INPUT, name) is None:
            raise Exception("Поле 'Имя' не найдено.")

        if self.send_keys_to_input(OrderFormLocators.SURNAME_INPUT, surname) is None:
            raise Exception("Поле 'Фамилия' не найдено.")

        if self.send_keys_to_input(OrderFormLocators.ADDRESS_INPUT, address) is None:
            raise Exception("Поле 'Адрес' не найдено.")

        if self.send_keys_to_input(OrderFormLocators.METRO_STATION_INPUT, metro_station) is None:
            raise Exception("Поле 'Станция метро' не найдено.")

        self.select_station()

        if self.send_keys_to_input(OrderFormLocators.PHONE_INPUT, phone) is None:
            raise Exception("Поле 'Телефон' не найдено.")

        self.click_to_element(OrderFormLocators.NEXT_BUTTON)

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_entry_second_form(self, date, comment):
        self.wait_visibility_of_element(OrderFormLocators.RENTAL_DATE_INPUT)
        self.send_keys_to_input(OrderFormLocators.RENTAL_DATE_INPUT, date)
        self.click_to_element(OrderFormLocators.BLACK_COLOR_CHECKBOX)
        self.click_to_element(OrderFormLocators.RENTAL_PERIOD_DROPDOWN)
        self.send_keys_to_input(OrderFormLocators.COMMENT_INPUT, comment)
        self.click_to_element(OrderFormLocators.FINAL_ORDER_BUTTON)
        self.wait_visibility_of_element(OrderFormLocators.BUTTON_YES)
        self.click_to_element(OrderFormLocators.BUTTON_YES)

    # Добавьте метод для проверки успешного оформления заказа
    @allure.step('Проверка успешности оформления заказа')
    def is_order_successful(self):
        return self.wait_visibility_of_element(OrderFormLocators.CONFIRMATION_MODAL) is not None

