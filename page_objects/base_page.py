from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
import pytest


class BasePage:
    def __init__(self, driver):
        """Инициализируем базовую страницу"""
        self.driver = driver

    @pytest.mark.usefixtures('driver')
    def wait_visibility_element(self, locator):
        """Ожидание видимости элемента по локатору"""
        WebDriverWait(self.driver, 150).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @pytest.mark.usefixtures('driver')
    def find_element(self, locator):
        """Возврат элемента по локатору"""
        return self.driver.find_element(*locator)

    @pytest.mark.usefixtures('driver')
    def scroll(self):
        """Скрол страницы вниз"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @pytest.mark.usefixtures('driver')
    def scroll_element(self, element):
        """Скрол к элементу"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @pytest.mark.usefixtures('driver')
    def receive_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url

    @pytest.mark.usefixtures('driver')
    def switch_to_window(self):
        """Переключение на другое окно"""
        return self.driver.switch_to.window(self.driver.window_handles[1])
