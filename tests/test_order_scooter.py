from data import ClientData1
from data import ClientData2
from locators import order_scooter_locators
from page_objects.order_scooter_page import OrderScooter
import pytest
import allure


class TestOrderScooter:

    @allure.title("Заказ самоката»")
    @allure.description(
        "Проверка всего флоу позитивного сценария с двумя наборами данных. Проверка точки входа в сценарий, "
        "их две: кнопка «Заказать» вверху страницы и внизу")
    @pytest.mark.parametrize(
        "name, surname, address, station, phone, date, rent, color, comment",
        [
            (
                    ClientData1.NAME1,
                    ClientData1.SURNAME1,
                    ClientData1.ADDRESS1,
                    order_scooter_locators.STATION_SOKOLNIKI,
                    ClientData1.PHONE1,
                    order_scooter_locators.DATA1_CHOOSE,
                    order_scooter_locators.RENT_TWO_DAYS,
                    order_scooter_locators.BLACK_COLOR_SCOOTER,
                    ClientData1.COMMENT1,
            ),
            (
                    ClientData2.NAME2,
                    ClientData2.SURNAME2,
                    ClientData2.ADDRESS2,
                    order_scooter_locators.STATION_OHOTNYI_RYAD,
                    ClientData2.PHONE2,
                    order_scooter_locators.DATA2_CHOOSE,
                    order_scooter_locators.RENT_FIVE_DAYS,
                    order_scooter_locators.GREY_COLOR_SCOOTER,
                    ClientData2.COMMENT2,
            ),
        ],
    )
    def test_order_scooter(
            self, driver, name, surname, address, station, phone, date, rent, color, comment
    ):
        """Тестовый заказ самоката"""
        order_scooter_page = OrderScooter(driver)
        order_scooter_page.click_order_button_upper()
        order_scooter_page.set_name_field(name)
        order_scooter_page.set_surname_field(surname)
        order_scooter_page.set_address_field(address)
        order_scooter_page.set_metro_station(station)
        order_scooter_page.set_phone_field(phone)
        order_scooter_page.click_next_button()
        order_scooter_page.set_delivery_date(date)
        order_scooter_page.set_rental_time(rent)
        order_scooter_page.set_color_scooter(color)
        order_scooter_page.set_comment(comment)
        order_scooter_page.click_order_button_lower()
        order_scooter_page.click_accept_button()
        assert order_scooter_page.get_text_status_button() == "Посмотреть статус", "Отсутствует кнопка 'Посмотреть'"
