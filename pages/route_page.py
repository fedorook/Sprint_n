import allure
from pages.base_page import BasePage
from locators.route_page_locators import RoutePageLocators


class RoutePage(BasePage):

    @allure.step("Check if route selection block is displayed")
    def check_route_selection_block_displayed(self):
        """Check that route selection block appears"""
        return (self.is_element_displayed(RoutePageLocators.OPTIMAL_TAB) and
                self.is_element_displayed(RoutePageLocators.FAST_TAB) and
                self.is_element_displayed(RoutePageLocators.CUSTOM_TAB))

    @allure.step("Check same address route text")
    def check_same_address_route_text(self):
        """Check that 'Авто Бесплатно' and 'В пути 0 мин.' are displayed"""
        free_auto_displayed = self.is_element_displayed(RoutePageLocators.FREE_AUTO_TEXT)
        zero_minutes_displayed = self.is_element_displayed(RoutePageLocators.ZERO_MINUTES_TEXT)
        return free_auto_displayed and zero_minutes_displayed

    @allure.step("Click on route type tab")
    def click_route_type(self, route_type):
        """Click on specific route type (optimal/fast/custom)"""
        route_locators = {
            "optimal": RoutePageLocators.OPTIMAL_TAB,
            "fast": RoutePageLocators.FAST_TAB,
            "custom": RoutePageLocators.CUSTOM_TAB
        }
        if route_type in route_locators:
            self.click_element(route_locators[route_type])
            if route_type == "custom":
                try:
                    self.wait_for_element_extended(RoutePageLocators.CAR_ICON, 10)
                except:
                    pass


    @allure.step("Check transportation types are active")
    def check_transportation_types_active(self):
        """Check that all transportation icons are displayed when Custom tab is selected"""
        return (self.is_element_displayed(RoutePageLocators.CAR_ICON) and
                self.is_element_displayed(RoutePageLocators.WALK_ICON) and
                self.is_element_displayed(RoutePageLocators.TAXI_ICON_ACTIVE) and
                self.is_element_displayed(RoutePageLocators.BIKE_ICON) and
                self.is_element_displayed(RoutePageLocators.SCOOTER_ICON) and
                self.is_element_displayed(RoutePageLocators.DRIVE_ICON))

    @allure.step("Check Call Taxi button is active")
    def check_call_taxi_button_active(self):
        """Check that Call Taxi button is displayed and clickable"""
        return (self.is_element_displayed(RoutePageLocators.CALL_TAXI_BUTTON) and
                self.check_element_is_clickable(RoutePageLocators.CALL_TAXI_BUTTON))

    @allure.step("Click Drive transportation option")
    def click_drive_option(self):
        """Click on Drive transportation icon"""
        self.click_element(RoutePageLocators.DRIVE_ICON)

    @allure.step("Check Book button is active for Drive")
    def check_book_button_active(self):
        """Check that Book button is displayed and clickable for Drive option"""
        return (self.is_element_displayed(RoutePageLocators.BOOK_BUTTON) and
                self.check_element_is_clickable(RoutePageLocators.BOOK_BUTTON))

    @allure.step("Click Call Taxi button")
    def click_call_taxi_button(self):
        """Click the Call Taxi button"""
        self.click_element(RoutePageLocators.CALL_TAXI_BUTTON)

    @allure.step("Get route price")
    def get_route_price(self):
        """Get the route price text"""
        return self.get_text_from_element(RoutePageLocators.PRICE)

    @allure.step("Get route duration")
    def get_route_duration(self):
        """Get the route duration text"""
        return self.get_text_from_element(RoutePageLocators.DURATION)

    @allure.step("Check route price visibility")
    def check_route_price_visibility(self):
        """Check that route price is displayed"""
        return self.is_element_displayed(RoutePageLocators.PRICE)

    @allure.step("Check route duration visibility")
    def check_route_duration_visibility(self):
        """Check that route duration is displayed"""
        return self.is_element_displayed(RoutePageLocators.DURATION)