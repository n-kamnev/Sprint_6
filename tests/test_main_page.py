import pytest
from locators import main_page_locators
from page_objects.main_page import MainPage
from page_objects.main_page import NavigationOnSite
from data import ModuleQuestionsAboutImportantAnswers
from selenium.webdriver.common.by import By
from data import Urls


class TestModuleQuestionsAboutImportant:

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
    def test_drop_down_list(self, driver, question, answer, true_answer):
        """Тестирование выпадающего списка в блоке 'Вопросы о важном' на главной странице"""
        question_main_page = MainPage(driver)
        question_main_page.scroll()
        button = question_main_page.wait_visibility_element((By.XPATH, "//div[@class='accordion__button']"))
        question_main_page.scroll_element(
            button)  # если убрать 60 и 61 строку? то программа будет работать не стабильно - не понимаю почему так
        question_main_page.wait_visibility_element(question)
        question_main_page.click_on_the_question(question)
        assert question_main_page.return_the_response_text(answer) == true_answer, "Неправильный ответ!!!"


class TestNavigationOnSite:

    def test_go_to_main_page_click_scooter_logo(self, driver):
        """Проверяем попадание на главную страницу, нажав лого Самокат"""
        navigation = NavigationOnSite(driver)
        navigation.click_order_button()
        navigation.click_logo_scooter()
        assert navigation.get_current_url() == Urls.MAIN_PAGE_SCOOTER

    def test_click_yandex_logo_redirect_on_dzen(self, driver):
        """Проверяем редирект на страницу Дзен"""
        navigation = NavigationOnSite(driver)
        navigation.click_yandex_logo()
        navigation.switch_on_tab()
        navigation.wait_visibility_search_button()
        assert navigation.get_current_url() == Urls.REDIRECT_DZEN
