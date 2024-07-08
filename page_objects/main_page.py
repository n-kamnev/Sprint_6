from locators import main_page_locators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        """Инициализируем главную страницу"""
        BasePage.__init__(self, driver)

    def scroll(self):
        """Скрол к элементу"""
        element = self.find_element(main_page_locators.SEVENTH_QUESTION)
        self.execute_script(element)

    def click_on_the_question(self, locator):
        """Клик по элементу"""
        element = self.find_element(locator)
        element.click()

    def return_the_response_text(self, locator):
        """Возврат текст ответа"""
        answer_text = self.find_element(locator)
        return answer_text.text
