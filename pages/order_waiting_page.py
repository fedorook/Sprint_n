import allure
from pages.base_page import BasePage
from locators.order_waiting_page_locators import OrderWaitingPageLocators


class OrderWaitingPage(BasePage):

    @allure.step("Check waiting window elements")
    def check_waiting_window_elements(self):
        """Check all elements in the car search waiting window"""
        elements = [
            OrderWaitingPageLocators.SEARCH_CAR_TITLE,
            OrderWaitingPageLocators.TIMER,
            OrderWaitingPageLocators.CANCEL_BUTTON,
            OrderWaitingPageLocators.DETAILS_BUTTON
        ]
        for element in elements:
            self.find_element_with_wait(element)
        return all(self.is_element_displayed(element) for element in elements)

    @allure.step("Check order completion window elements")
    def check_order_completion_elements(self):
        """Check all elements in the completed order window"""
        elements = [
            ("CAR_IMAGE", OrderWaitingPageLocators.CAR_IMAGE),
            ("DRIVER_NAME", OrderWaitingPageLocators.DRIVER_NAME),
            ("DRIVER_AVATAR", OrderWaitingPageLocators.DRIVER_AVATAR),
            ("DRIVER_RATING", OrderWaitingPageLocators.DRIVER_RATING)
        ]
        for name, element in elements:
            try:
                self.find_element_with_wait(element)
                print(f"✓ Found {name}")
            except Exception as e:
                print(f"✗ Failed to find {name}: {e}")
                return False
        return all(self.is_element_displayed(element) for _, element in elements)

    @allure.step("Click laptop table checkbox")
    def click_laptop_table_checkbox(self):
        """Click the 'Столик для ноутбука' checkbox"""
        self.scroll_to_element(OrderWaitingPageLocators.ORDER_REQUIREMENTS)
        self.click_element(OrderWaitingPageLocators.ORDER_REQUIREMENTS)
        self.click_element(OrderWaitingPageLocators.LAPTOP_TABLE_CHECKBOX)

    @allure.step("Click order now button")
    def click_order_now_button(self):
        """Click 'Ввести номер и заказать' button"""
        self.click_element(OrderWaitingPageLocators.ORDER_NOW_BUTTON)

    @allure.step("Wait for timer to complete")
    def wait_for_timer_completion(self):
        """Wait for the search timer to complete (30+ seconds)"""
        # Wait for timer to disappear or for order completion elements to appear
        return self.wait_for_element_extended(OrderWaitingPageLocators.ORDER_TITLE, timeout=35)

    @allure.step("Click details button")
    def click_details_button(self):
        """Click the Details button"""
        self.click_element(OrderWaitingPageLocators.DETAILS_BUTTON)

    @allure.step("Click cancel button")
    def click_cancel_button(self):
        """Click the Cancel button"""
        self.click_element(OrderWaitingPageLocators.CANCEL_BUTTON)

    @allure.step("Check if waiting window disappeared")
    def check_waiting_window_disappeared(self):
        """Check that the waiting window is no longer visible"""
        return self.wait_for_element_to_disappear(OrderWaitingPageLocators.WAITING_WINDOW)