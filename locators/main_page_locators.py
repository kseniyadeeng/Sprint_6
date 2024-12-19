from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локаторы для cookie и логотипов
    BUTTON_COOKIES = (By.XPATH, '//*[contains(@class, "App_CookieButton_")]')  # Локатор cookie
    SCOOTER_LOGO = (By.XPATH, '//a[contains(@class, "Header_LogoScooter__")]/img[@alt="Scooter"]')  # логотип Самоката
    HEADER_YANDEX_LOGO = (By.XPATH, '//a[contains(@class, "Header_LogoYandex__")]/img[@alt="Yandex"]')  # Логотип Яндекс

    # Локаторы кнопок "Заказать" и кнопки Поиска
    BUTTON_ORDER_IN_MIDDLE = (By.XPATH, '//*[contains(@class, "Button_Middle") and text()="Заказать"]')  # Кнопка "Заказать" в середине страницы
    BUTTON_ORDER_HEADER = (By.XPATH, '//*[contains(@class, "Header_Nav")]/child::button[text()="Заказать"]')  # Кнопка "Заказать" в хедере
    BUTTON_SEARCH = (By.XPATH, '//div[contains(@class, "Header_SearchInput__")]/button[text()="Go!"]')

    # Локаторы для кнопок "Статус заказа"
    BUTTON_STATUS_ORDER = (By.XPATH, '//div[contains(@class, "Header_Nav__AGCXC")]//button[text()="Статус заказа"]')

    # Локатор для заголовка "Вопросы о важном"
    IMPORTANT_QUESTIONS_HEADER = (By.XPATH, '//div[contains(@class, "Home_SubHeader__zwi_E") and text()="Вопросы о важном"]')

    # Локатор для аккордеона вопросов
    FAQ_ACCORDION = (By.XPATH, '//div[@data-accordion-component="Accordion"]')

    # Локаторы для вкладки "Вопросы"
    FAQ_SECTION = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')  # Вкладка вопросы

    # Локаторы вопросов FAQ
    FAQ_QUESTIONS = {
        'QUESTION_1': (By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'),  # Вопрос 1
        'QUESTION_2': (By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'),  # Вопрос 2
        'QUESTION_3': (By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'),  # Вопрос 3
        'QUESTION_4': (By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'),  # Вопрос 4
        'QUESTION_5': (By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'),  # Вопрос 5
        'QUESTION_6': (By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'),  # Вопрос 6
        'QUESTION_7': (By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'),  # Вопрос 7
        'QUESTION_8': (By.XPATH, '//div[@id="accordion__heading-7"]/parent::div')  # Вопрос 8
    }

    # Локаторы ответов FAQ
    FAQ_ANSWERS = {
        'ANSWER_1': (By.XPATH, '//div[@id="accordion__panel-0"]'),  # Ответ 1
        'ANSWER_2': (By.XPATH, '//div[@id="accordion__panel-1"]'),  # Ответ 2
        'ANSWER_3': (By.XPATH, '//div[@id="accordion__panel-2"]'),  # Ответ 3
        'ANSWER_4': (By.XPATH, '//div[@id="accordion__panel-3"]'),  # Ответ 4
        'ANSWER_5': (By.XPATH, '//div[@id="accordion__panel-4"]'),  # Ответ 5
        'ANSWER_6': (By.XPATH, '//div[@id="accordion__panel-5"]'),  # Ответ 6
        'ANSWER_7': (By.XPATH, '//div[@id="accordion__panel-6"]'),  # Ответ 7
        'ANSWER_8': (By.XPATH, '//div[@id="accordion__panel-7"]')  # Ответ 8
    }