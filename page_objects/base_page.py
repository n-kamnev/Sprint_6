from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание видимости элемента по локатору")
    @pytest.mark.usefixtures('driver')
    def wait_visibility_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step("Возврат элемента по локатору")
    @pytest.mark.usefixtures('driver')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Скрол страницы вниз")
    @pytest.mark.usefixtures('driver')
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Скрол к элементу")
    @pytest.mark.usefixtures('driver')
    def scroll_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получение текущего URL")
    @pytest.mark.usefixtures('driver')
    def receive_current_url(self):
        return self.driver.current_url

    @allure.step("Переключение на другое окно")
    @pytest.mark.usefixtures('driver')
    def switch_to_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
