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
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @pytest.mark.usefixtures('driver')
    def find_element(self, locator):
        """Возврат элемента по локатору"""
        return self.driver.find_element(*locator)

    @pytest.mark.usefixtures('driver')
    def execute_script(self, element):
        """Выполняет скрипт scrollIntoView для скрола к элементу"""
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)
