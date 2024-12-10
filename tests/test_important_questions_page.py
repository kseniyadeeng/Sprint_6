import allure
import pytest
from ..conftest import driver
from data import Answer
from pages.main_page import MainPage


class TestQuestionsMainPage:

    @allure.title('Проверяем вопросы и ответы на главной странице')
    @allure.description('Кликаем на вопросы и проверяем ответы в списке')
    @pytest.mark.parametrize("question_key, expected_answer",
                             [('QUESTION_1', Answer.answer_1),
                              ('QUESTION_2', Answer.answer_2),
                              ('QUESTION_3', Answer.answer_3),
                              ('QUESTION_4', Answer.answer_4),
                              ('QUESTION_5', Answer.answer_5),
                              ('QUESTION_6', Answer.answer_6),
                              ('QUESTION_7', Answer.answer_7),
                              ('QUESTION_8', Answer.answer_8)]
                             )
    def test_questions(self, driver, question_key, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_item(question_key)
        main_page.click_on_faq_item(question_key)
        main_page.wait_visibility_of_faq_answer(question_key.replace('QUESTION', 'ANSWER'))
        result = main_page.get_displayed_text_from_faq_answer(question_key.replace('QUESTION', 'ANSWER'))

        assert result == expected_answer
