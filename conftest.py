from selenium import webdriver
import pytest
from data import Urls
from page_objects.main_page import MainPage
from page_objects.main_page import NavigationOnSite
from page_objects.order_scooter_page import OrderScooter

firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--headless")
firefox_options.add_argument("--ignore-certificate-errors")
firefox_options.add_argument("--disable-cache")
firefox_options.add_argument("--disable-blink-features=AutomationControlled")
firefox_options.add_argument(
    "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (HTML, like Gecko) "
    "Chrome/125.0.0.0 Safari/537.3"
    "")


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера Firefox и перехода на главную страницу"""
    firefox_driver = webdriver.Firefox(options=firefox_options)
    firefox_driver.get(Urls.MAIN_PAGE_SCOOTER)
    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture(scope="function")
def page(driver):
    page = MainPage(driver)
    yield page


@pytest.fixture(scope="function")
def page_two(driver):
    page = OrderScooter(driver)
    yield page


@pytest.fixture(scope="function")
def page_three(driver):
    page = NavigationOnSite(driver)
    yield page
