import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.route_page_locators import RoutePageLocators
from test_data import URL


class MainPage(BasePage):

    @allure.step("Open Yandex Routes application")
    def open_yandex_routes(self):
        """Navigate to Yandex Routes main page"""
        self.go_to_url(URL)

    @allure.step("Check if route points are displayed on map")
    def check_route_points_displayed(self):
        """Check that both A and B points are visible on the map"""
        try:
            self.wait_for_element_extended(MainPageLocators.A_POINT, 15)
            self.wait_for_element_extended(MainPageLocators.B_POINT, 15)
            return True
        except:
            return False

    @allure.step("Enter addresses for route")
    def enter_route_addresses(self, from_address, to_address):
        """Enter from and to addresses"""
        self.add_text_to_element(MainPageLocators.FROM_FIELD, from_address)
        self.add_text_to_element(MainPageLocators.TO_FIELD, to_address)

    @allure.step("Enter different addresses")
    def enter_different_addresses(self):
        """Enter different preset addresses in from and to fields"""
        super().enter_different_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)
        self.wait_for_route_calculation()

    @allure.step("Wait for route calculation")
    def wait_for_route_calculation(self):
        """Wait for route to be calculated and route selection block to appear"""
        try:
            self.wait_for_element_extended(RoutePageLocators.OPTIMAL_TAB, 15)
        except:
            pass

    @allure.step("Enter same addresses")
    def enter_same_addresses(self):
        """Enter same preset address in both from and to fields"""
        super().enter_same_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)

