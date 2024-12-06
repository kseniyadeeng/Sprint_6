from selenium.webdriver.common.by import By

class OrderFormLocators:
    # Локаторы для формы "Для кого самокат"
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')  # Поле "Имя"
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')  # Поле "Фамилия"
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')  # Поле "Адрес"
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Поле "Станция метро"
    SELECT_ITEM_IN_DROPDOWN_METRO = (By.XPATH, ".//li[@class='select-search__row']")  # Элемент в дропдауне
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  # Поле "Телефон"
    NEXT_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text()="Далее"]')  # Кнопка "Далее"

    # Локаторы для формы "Про аренду"
    RENTAL_DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')  # Поле "Когда привезти самокат"
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, '//div[@class="Dropdown-control"]')  # Дропдаун "Срок аренды"
    CALENDAR = (By.XPATH, "//div[@class='react-datepicker-popper']")  # Календарь
    CALENDAR_ITEM = (
    By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")  # Элемент календаря
    BLACK_COLOR_CHECKBOX = (By.XPATH, '//label[@for="black"]')  # Чекбокс "Чёрный жемчуг"
    GREY_COLOR_CHECKBOX = (By.XPATH, '//label[@for="grey"]')  # Чекбокс "Серая безысходность"
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')  # Поле "Комментарий для курьера"
    BACK_BUTTON = (By.XPATH, '//button[contains(text(), "Назад")]')  # Кнопка "Назад"
    FINAL_ORDER_BUTTON = (By.XPATH,
                          '//button[contains(text(), "Заказать") and not(contains(@class, "Button_Inverted__3IF-i"))]')  # Кнопка "Заказать"

    # Локаторы для окна подтверждения заказа
    CONFIRMATION_MODAL = (By.XPATH, '//div[contains(@class, "Order_Modal__YZ-d3")]')  # Модальное окно подтверждения
    CONFIRMATION_HEADER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader__3FDaJ")]')  # Заголовок модального окна
    BUTTON_NO = (
    By.XPATH, '//button[contains(text(), "Нет") and contains(@class, "Button_Inverted__3IF-i")]')  # Кнопка "Нет"
    BUTTON_YES = (
    By.XPATH, '//button[contains(text(), "Да") and not(contains(@class, "Button_Inverted__3IF-i"))]')  # Кнопка "Да"
    BUTTON_CHECK_STATUS_OF_ORDER = (By.XPATH, ".//*[text()='Посмотреть статус']")  # Кнопка "Посмотреть статус"
    BUTTON_COOKIES = (By.XPATH, '//*[contains(@class, "App_CookieButton_")]')  # Локатор cookiess='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")