import allure
import pytest
from locators import main_page_locators
from data import ModuleQuestionsAboutImportantAnswers
from data import Urls


class TestModuleQuestionsAboutImportant:

    @allure.title("Выпадающий список в разделе «Вопросы о важном»")
    @allure.description("При нажатии на стрелочку, открывается соответствующий текст")
    @pytest.mark.parametrize(
        "question, answer, true_answer",
        [
            (
                    main_page_locators.FIRST_QUESTION,
                    main_page_locators.FIRST_QUESTION_OPEN,
                    ModuleQuestionsAboutImportantAnswers.FIRST_QUESTION_ANSWER,
            ),
            (
                    main_page_locators.SECOND_QUESTION,
                    main_page_locators.SECOND_QUESTION_OPEN,
                    ModuleQuestionsAboutImportantAnswers.SECOND_QUESTION_ANSWER,
            ),
            (
                    main_page_locators.THIRD_QUESTION,
                    main_page_locators.THIRD_QUESTION_OPEN,
                    ModuleQuestionsAboutImportantAnswers.THIRD_QUESTION_ANSWER,
            ),
            (
                    main_page_locators.FOURTH_QUESTION,
                    main_page_locators.FOURTH_QUESTION_OPEN,
                    ModuleQuestionsAboutImportantAnswers.FOURTH_QUESTION_ANSWER,
            ),
            (
                    main_page_locators.FIFTH_QUESTION,
                    main_page_locators.FIFTH_QUESTION_OPEN,
                    ModuleQuestionsAboutImportantAnswers.FIFTH_QUESTION_ANSWER,
            ),
            (
                    main_page_locators.SIXTH_QUESTION,
                    main_page_locators.SIXTH_QUESTION_OPEN,
                    ModuleQuestionsAboutImportantAnswers.SIXTH_QUESTION_ANSWER,
            ),
            (
                    main_page_locators.SEVENTH_QUESTION,
                    main_page_locators.SEVENTH_QUESTION_OPEN,
                    ModuleQuestionsAboutImportantAnswers.SEVENTH_QUESTION_ANSWER,
            ),
            (
                    main_page_locators.EIGHTH_QUESTION,
                    main_page_locators.EIGHTH_QUESTION_OPEN,
                    ModuleQuestionsAboutImportantAnswers.EIGHT_QUESTION_ANSWER,
            )
        ]
    )
    def test_drop_down_list(self, page, question, answer, true_answer):
        page.scroll()
        button = page.wait_visibility_element(question, 15)
        page.scroll_element(button)
        page.wait_visibility_element(question)
        page.click_on_the_question(question)
        assert page.return_the_response_text(answer) == true_answer, "Неправильный ответ!!!"


class TestNavigationOnSite:

    @allure.title("Переход на главную страницу при нажатии на логотип 'Самокат'")
    @allure.description("При нажатии на логотип «Самоката», попадёшь на главную страницу «Самоката»")
    def test_go_to_main_page_click_scooter_logo(self, page_three):
        page_three.click_order_button()
        page_three.click_logo_scooter()
        assert page_three.get_current_url() == Urls.MAIN_PAGE_SCOOTER

    @allure.title("Редирект на страницу Дзен при нажатии на логотип 'Яндекс'")
    @allure.description(
        "При нажатии на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена")
    def test_click_yandex_logo_redirect_on_dzen(self, page_three):
        page_three.click_yandex_logo()
        page_three.switch_on_tab()
        page_three.wait_visibility_search_button()
        assert page_three.get_current_url() == Urls.REDIRECT_DZEN
