import pytest
import allure
from ..conftest import driver
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import TestDataUsers


class TestOrder:
    @allure.title('Позитивная проверка оформления заказа')
    @allure.description('Проверка оформления заказа')
    @pytest.mark.parametrize(
        'button, name, surname, address, metro_station, phone, date, comment',
        [
            (MainPageLocators.BUTTON_ORDER_HEADER,
             TestDataUsers.user1_name,
             TestDataUsers.user1_surname,
             TestDataUsers.user1_address,
             TestDataUsers.user1_metro_station,
             TestDataUsers.user1_phone,
             TestDataUsers.user1_date,
             TestDataUsers.user1_comment),
            (MainPageLocators.BUTTON_ORDER_IN_MIDDLE,
             TestDataUsers.user2_name,
             TestDataUsers.user2_surname,
             TestDataUsers.user2_address,
             TestDataUsers.user2_metro_station,
             TestDataUsers.user2_phone,
             TestDataUsers.user2_date,
             TestDataUsers.user2_comment)
        ]
    )
    def test_order_all_fields_success(self, driver, button, name, surname, address, metro_station, phone, date,
                                      comment):
        order_page = OrderPage(driver)

        # Прокрутка к кнопке "Заказать"
        order_page.scroll_to_element(button)

        # Ожидание видимости кнопки и её нажатие
        order_page.wait_visibility_of_element(button)
        order_page.click_to_element(button)

        # Заполнение первой формы заказа
        order_page.data_entry_first_form(name, surname, address, metro_station, phone)

        # Заполнение второй части формы заказа
        order_page.data_entry_second_form(date, comment)

        # Проверка отображения кнопки проверки статуса заказа
        assert order_page.check_displaying_of_button_check_status_of_order()
