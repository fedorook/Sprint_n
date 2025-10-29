import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Check if route points are displayed on map")
    def check_route_points_displayed(self):
        """Check that both A and B points are visible on the map"""
        a_point_displayed = self.is_element_displayed(MainPageLocators.A_POINT)
        b_point_displayed = self.is_element_displayed(MainPageLocators.B_POINT)
        return a_point_displayed and b_point_displayed

    @allure.step("Enter addresses for route")
    def enter_route_addresses(self, from_address, to_address):
        """Enter from and to addresses"""
        self.add_text_to_element(MainPageLocators.FROM_FIELD, from_address)
        self.add_text_to_element(MainPageLocators.TO_FIELD, to_address)

    @allure.step("Enter different addresses")
    def enter_different_addresses(self):
        """Enter different preset addresses in from and to fields"""
        super().enter_different_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)

    @allure.step("Enter same addresses")
    def enter_same_addresses(self):
        """Enter same preset address in both from and to fields"""
        super().enter_same_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)