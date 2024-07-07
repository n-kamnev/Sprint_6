from selenium import webdriver
import pytest
from data import Urls


@pytest.fixture(scope="function")
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(Urls.MAIN_PAGE_SCOOTER)
    yield firefox_driver
    firefox_driver.quit()
