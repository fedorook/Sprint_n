import allure
from pages.base_page import BasePage
from locators.taxi_order_page_locators import TaxiOrderPageLocators
from test_data import TAXI_TARIFF_DESCRIPTIONS


class TaxiOrderPage(BasePage):

    @allure.step("Check all 6 taxi tariffs are displayed")
    def check_all_tariffs_displayed(self):
        """Check that all 6 taxi tariffs are visible"""
        tariffs = [
            TaxiOrderPageLocators.WORKING_TARIFF,
            TaxiOrderPageLocators.SLEEPY_TARIFF,
            TaxiOrderPageLocators.VACATION_TARIFF,
            TaxiOrderPageLocators.TALKATIVE_TARIFF,
            TaxiOrderPageLocators.CONSOLATION_TARIFF,
            TaxiOrderPageLocators.GLOSSY_TARIFF
        ]
        return all(self.is_element_displayed(tariff) for tariff in tariffs)

    @allure.step("Check if one tariff is active")
    def check_one_tariff_is_active(self):
        """Check that one of the tariffs has active state"""
        tariff_cards = self.wait_for_elements(TaxiOrderPageLocators.ALL_TARIFF_CARDS)
        active_tariffs = []
        for card in tariff_cards:
            class_attr = card.get_attribute("class")
            if "active" in class_attr:
                active_tariffs.append(card)
        return len(active_tariffs) > 0

    @allure.step("Click on tariff")
    def click_tariff(self, tariff_name):
        """Click on specific tariff by name"""
        tariff_locators = {
            "Рабочий": TaxiOrderPageLocators.WORKING_TARIFF,
            "Сонный": TaxiOrderPageLocators.SLEEPY_TARIFF,
            "Отпускной": TaxiOrderPageLocators.VACATION_TARIFF,
            "Разговорчивый": TaxiOrderPageLocators.TALKATIVE_TARIFF,
            "Утешительный": TaxiOrderPageLocators.CONSOLATION_TARIFF,
            "Глянцевый": TaxiOrderPageLocators.GLOSSY_TARIFF
        }
        if tariff_name in tariff_locators:
            self.click_element(tariff_locators[tariff_name])

    @allure.step("Hover over tariff info icon")
    def hover_over_tariff_info(self):
        """Hover over the 'i' icon to see tariff description"""
        self.hover_over_element(TaxiOrderPageLocators.TARIFF_INFO_BUTTON)

    @allure.step("Get tariff description")
    def get_tariff_description(self):
        """Get the text from the tariff description popup"""
        return self.get_text_from_element(TaxiOrderPageLocators.TARIFF_DESCRIPTION)

    @allure.step("Check tariff description matches expected")
    def check_tariff_description(self, tariff_name, description):
        """Verify tariff description matches expected text from test data"""
        expected_description = TAXI_TARIFF_DESCRIPTIONS.get(tariff_name)
        return description == expected_description

    @allure.step("Check order form fields are displayed")
    def check_order_form_fields_displayed(self):
        """Check that all order form fields are visible"""
        fields = [
            TaxiOrderPageLocators.PHONE_FIELD,
            TaxiOrderPageLocators.PAYMENT_METHOD_FIELD,
            TaxiOrderPageLocators.COMMENT_FIELD,
            TaxiOrderPageLocators.ORDER_REQUIREMENTS_FIELD
        ]
        return all(self.is_element_displayed(field) for field in fields)

    @allure.step("Click order button")
    def click_order_button(self):
        """Click the 'Ввести номер и заказать' button"""
        self.click_element(TaxiOrderPageLocators.ORDER_BUTTON)