import allure
from ..conftest import driver
from pages.main_page import MainPage


class TestLogo:
   @allure.title('Проверка перехода на главную страницу сервиса при клике на логотип Самокат')
   def test_logo_redirect_to_main_page_success(self, driver):
       main_page = MainPage(driver)
       main_page.wait_visibility_of_order_button_header()
       main_page.click_on_order_button_header()
       main_page.wait_visibility_of_header_logo_scooter()
       main_page.click_on_header_logo_scooter()
       main_page.wait_visibility_of_main_header()
       assert main_page.check_displaying_of_main_header()


   @allure.title('Проверка перехода на страницу "Дзена" при клике на логотип "Яндекс"')
   def test_logo_redirect_to_dzen_success(self, driver):
       main_page = MainPage(driver)
       main_page.wait_visibility_of_header_logo_yandex()
       main_page.click_on_header_logo_yandex()
       main_page.switch_to_next_tab()
       main_page.wait_for_title_to_be('Дзен')
       assert main_page.get_page_title() == 'Дзен'
