from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure


class BasePage:
    def __init__(self, driver):
        """Инициализируем базовую страницу"""
        self.driver = driver

    @allure.step("Ожидание видимости элемента по локатору")
    @pytest.mark.usefixtures('driver')
    def wait_visibility_element(self, locator):
        """Ожидание видимости элемента по локатору"""
        WebDriverWait(self.driver, 150).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Возврат элемента по локатору")
    @pytest.mark.usefixtures('driver')
    def find_element(self, locator):
        """Возврат элемента по локатору"""
        return self.driver.find_element(*locator)

    @allure.step("Скрол страницы вниз")
    @pytest.mark.usefixtures('driver')
    def scroll(self):
        """Скрол страницы вниз"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Скрол к элементу")
    @pytest.mark.usefixtures('driver')
    def scroll_element(self, element):
        """Скрол к элементу"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получение текущего URL")
    @pytest.mark.usefixtures('driver')
    def receive_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url

    @allure.step("Переключение на другое окно")
    @pytest.mark.usefixtures('driver')
    def switch_to_window(self):
        """Переключение на другое окно"""
        return self.driver.switch_to.window(self.driver.window_handles[1])
