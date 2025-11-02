import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
        for tariff in tariffs:
            self.find_element_with_wait(tariff)
        return all(self.is_element_displayed(tariff) for tariff in tariffs)

    @allure.step("Check if one tariff is active")
    def check_one_tariff_is_active(self):
        """Check that one of the tariffs has active state"""
        tariffs = [
            TaxiOrderPageLocators.WORKING_TARIFF,
            TaxiOrderPageLocators.SLEEPY_TARIFF,
            TaxiOrderPageLocators.VACATION_TARIFF,
            TaxiOrderPageLocators.TALKATIVE_TARIFF,
            TaxiOrderPageLocators.CONSOLATION_TARIFF,
            TaxiOrderPageLocators.GLOSSY_TARIFF
        ]
        active_tariffs = 0
        for tariff in tariffs:
            self.find_element_with_wait(tariff)
            tariff_element = self.driver.find_element(*tariff)
            parent_card = tariff_element.find_element(By.XPATH, "./..")
            class_attr = parent_card.get_attribute("class")
            if "active" in class_attr:
                active_tariffs += 1
        return active_tariffs > 0

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
        return self.get_text_from_element(tuple(TaxiOrderPageLocators.TARIFF_DESCRIPTION))

    @allure.step("Check tariff description matches expected")
    def check_tariff_description(self, tariff_name, description):
        """Verify tariff description matches expected text from test data"""
        expected_description = TAXI_TARIFF_DESCRIPTIONS.get(tariff_name)
        return description == expected_description

    @allure.step("Check order form fields are displayed")
    def check_order_form_fields_displayed(self):
        """Check that all order form fields are visible"""
        try:
            self.find_element_with_wait(TaxiOrderPageLocators.PHONE_FIELD)
            self.find_element_with_wait(TaxiOrderPageLocators.PAYMENT_METHOD_FIELD)
            self.find_element_with_wait(TaxiOrderPageLocators.COMMENT_FIELD)
            self.find_element_with_wait(TaxiOrderPageLocators.ORDER_REQUIREMENTS_FIELD)
            return True
        except:
            return False

    @allure.step("Click order button")
    def click_order_button(self):
        """Click the 'Ввести номер и заказать' button"""
        self.click_element(TaxiOrderPageLocators.ORDER_BUTTON)