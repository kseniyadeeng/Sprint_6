from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидаем видимость элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Кликнуть по элементу')
    def click_to_element(self, locator):
        self.wait_visibility_of_element(locator)  # Исправлено здесь
        self.driver.find_element(*locator).click()

    @allure.step('Ввести текст')
    def add_text_to_element(self, locator, text):
        self.wait_visibility_of_element(locator)  # Исправлено здесь
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текст')
    def get_text_from_element(self, locator):
        self.wait_visibility_of_element(locator)  # Исправлено здесь
        return self.driver.find_element(*locator).text

    @allure.step('Прокрутить к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить заголовок страницы')
    def get_page_title(self):
        return self.driver.title

    @allure.step('Подождать открытия новой вкладки')
    def wait_for_new_window(self, url):
        WebDriverWait(self.driver, 15).until(EC.url_to_be(url))

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.find_element_with_wait(locator).is_displayed()

    @allure.step('Подождать исчезновения элемента')
    def wait_element_until_not_visible(self, locator):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    def send_keys_to_input(self, locator, text):
        element = self.wait_visibility_of_element(locator)
        element.clear()
        element.send_keys(text)

    def send_keys_to_input(self, locator, text):
        element = self.wait_visibility_of_element(locator)
        if element:
            element.clear()
            element.send_keys(text)
            return element
        else:
            return None
