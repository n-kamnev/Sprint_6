from locators import order_scooter_locators
from page_objects.base_page import BasePage


class OrderScooter(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_order_button_upper(self):
        """Клик на кнопку 'Заказать самокат'"""
        button = self.find_element(order_scooter_locators.ORDER_BUTTON_UPPER)
        button.click()

    def set_name_field(self, name):
        """Заполнение поля 'Имя'"""
        name_input = self.find_element(order_scooter_locators.NAME_FIELD)
        name_input.send_keys(name)

    def set_surname_field(self, surname):
        """Заполнение поля 'Фамилия'"""
        surname_input = self.find_element(order_scooter_locators.SURNAME_FIELD)
        surname_input.send_keys(surname)

    def set_address_field(self, address):
        """Заполнение поля 'Адрес: куда привезти заказ'"""
        address_input = self.find_element(order_scooter_locators.ADDRESS_FIELD)
        address_input.send_keys(address)

    def set_metro_station(self, locator):
        """"Заполнение поля 'Станция метро'"""
        station = self.find_element(order_scooter_locators.METRO_FIELD)
        station.click()
        selected_station = self.find_element(locator)
        selected_station.click()

    def set_phone_field(self, phone):
        """Заполнение поля 'Телефон: на него позвонит курьер'"""
        phone_input = self.find_element(order_scooter_locators.PHONE_FIELD)
        phone_input.send_keys(phone)

    def click_next_button(self):
        """Клик на кнопку 'Далее'"""
        next_button = self.find_element(order_scooter_locators.NEXT_BUTTON)
        next_button.click()

    def set_delivery_date(self, locator):
        """Заполнение поля 'Когда привезти'"""
        date_field = self.find_element(order_scooter_locators.DATE_FIELD)
        date_field.click()
        selected_date = self.find_element(locator)
        selected_date.click()

    def set_rental_time(self, locator):
        """Заполнение поля 'Время аренды'"""
        rental_field = self.find_element(order_scooter_locators.RENTAL_TIME_FIELD)
        rental_field.click()
        selected_rental_field = self.find_element(locator)
        selected_rental_field.click()

    def set_color_scooter(self, locator):
        """Цвет самоката"""
        scooter_color = self.find_element(locator)
        scooter_color.click()

    def set_comment(self, comment):
        """Комментарий для курьера"""
        comment_input = self.find_element(order_scooter_locators.COMMENT_FIELD)
        comment_input.send_keys(comment)

    def click_order_button_lower(self):
        """Клик на кнопку 'Заказать'"""
        button = self.find_element(order_scooter_locators.ORDER_BUTTON_LOWER)
        button.click()

    def click_accept_button(self):
        """Клик на кнопку 'Да' при подтверждении заказа"""
        accept_button = self.find_element(order_scooter_locators.ACCEPT_BUTTON)
        accept_button.click()

    def get_text_status_button(self):
        """Получение текста кнопки 'Посмотреть'"""
        status_button = self.find_element(order_scooter_locators.SEE_STATUS_BUTTON)
        return status_button.text
