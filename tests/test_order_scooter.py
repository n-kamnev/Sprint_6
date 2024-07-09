from data import ClientData1
from data import ClientData2
from data import NameButton
from locators import order_scooter_locators
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
            self, page_two, name, surname, address, station, phone, date, rent, color, comment
    ):
        page_two.click_order_button_upper()
        page_two.set_name_field(name)
        page_two.set_surname_field(surname)
        page_two.set_address_field(address)
        page_two.set_metro_station(station)
        page_two.set_phone_field(phone)
        page_two.click_next_button()
        page_two.set_delivery_date(date)
        page_two.set_rental_time(rent)
        page_two.set_color_scooter(color)
        page_two.set_comment(comment)
        page_two.click_order_button_lower()
        page_two.click_accept_button()
        assert page_two.get_text_status_button() == NameButton.NAME_BUTTON, "Отсутствует кнопка 'Посмотреть'"
