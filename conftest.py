from selenium import webdriver
import pytest
from data import Urls

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--ignore-certificate-errors')
firefox_options.add_argument('--disable-cache')
# firefox_options.add_argument('--window-size=1920,1080')
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHT, like Gecko)')


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания драйвера Firefox и перехода на главную страницу"""
    firefox_driver = webdriver.Firefox(options=firefox_options)
    firefox_driver.get(Urls.MAIN_PAGE_SCOOTER)
    yield firefox_driver
    firefox_driver.quit()
