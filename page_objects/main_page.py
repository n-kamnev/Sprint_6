from page_objects.base_page import BasePage
from locators import main_page_locators
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        """Инициализируем главную страницу"""
        BasePage.__init__(self, driver)

    @allure.step("Клик по элементу")
    def click_on_the_question(self, locator):
        """Клик по элементу"""
        element = self.find_element(locator)
        element.click()

    @allure.step("Возврат текст ответа")
    def return_the_response_text(self, locator):
        """Возврат текст ответа"""
        answer_text = self.find_element(locator)
        return answer_text.text


class NavigationOnSite(BasePage):
    @allure.step("Клик по логотипу Самоката")
    def click_logo_scooter(self):
        """Клик по логотипу Самоката"""
        logo_scooter = self.find_element(main_page_locators.SCOOTER_LOGO)
        logo_scooter.click()

    @allure.step("Клик по верхней кнопке заказать")
    def click_order_button(self):
        """Клик по верхней кнопке заказать"""
        order_button = self.find_element(main_page_locators.TOP_ORDER_BUTTON)
        order_button.click()

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        """Получение текущего URL"""
        return self.receive_current_url()

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        yandex_logo = self.find_element(main_page_locators.YANDEX_LOGO)
        yandex_logo.click()

    @allure.step("Переключение на другое окно")
    def switch_on_tab(self):
        """Переключение на другое окно"""
        self.switch_to_window()

    @allure.step("Ожидание видимости кнопки поиска Дзен")
    def wait_visibility_search_button(self):
        """Ожидание видимости кнопки поиска Дзен"""
        self.wait_visibility_element(main_page_locators.DZEN_SEARCH_BUTTON)
        return self.find_element(main_page_locators.DZEN_SEARCH_BUTTON)
