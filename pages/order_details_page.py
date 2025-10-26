import allure
from pages.base_page import BasePage
from locators.order_details_page_locators import OrderDetailsPageLocators


class OrderDetailsPage(BasePage):

    @allure.step("Get tariff price")
    def get_tariff_price(self):
        """Get the price displayed on the tariff card"""
        return self.get_text_from_element(OrderDetailsPageLocators.TARIFF_PRICE)

    @allure.step("Get price from details")
    def get_price_from_details(self):
        """Get the price shown in the details section"""
        return self.get_text_from_element(OrderDetailsPageLocators.PRICE_IN_DETAILS)

    @allure.step("Check if tariff price matches details price")
    def check_price_consistency(self):
        """Verify that tariff price matches the price in details"""
        tariff_price = self.get_tariff_price()
        details_price = self.get_price_from_details()
        return tariff_price in details_price or details_price in tariff_price

    @allure.step("Check details window elements")
    def check_details_window_elements(self):
        """Check that all required elements are present in details window"""
        elements = [
            OrderDetailsPageLocators.PICKUP_ADDRESS,
            OrderDetailsPageLocators.DESTINATION_ADDRESS,
            OrderDetailsPageLocators.PAYMENT_METHOD,
            OrderDetailsPageLocators.TRIP_INFO_TITLE,
            OrderDetailsPageLocators.COST_INFO
        ]
        return all(self.is_element_displayed(element) for element in elements)

    @allure.step("Click cancel button")
    def click_cancel_button(self):
        """Click the Cancel button to close the window"""
        self.click_element(OrderDetailsPageLocators.CANCEL_BUTTON)