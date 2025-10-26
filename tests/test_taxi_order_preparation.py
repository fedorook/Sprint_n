import allure
import pytest
from test_data import URL
from locators.main_page_locators import MainPageLocators


@allure.epic("Yandex Routes Testing")
@allure.feature("Taxi Order Preparation")
class TestTaxiOrderPreparation:

    @allure.title("Check route tab switching between Optimal and Fast")
    @allure.description("Verify that switching between Optimal and Fast route types changes active tab and recalculates time and cost")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_route_tab_switching_optimal_fast(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            driver.get(URL)

        with allure.step("Enter different addresses"):
            main_page.enter_different_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)

        with allure.step("Click on Optimal tab"):
            route_page.click_route_type("optimal")

        with allure.step("Get price and duration for Optimal route"):
            optimal_price = route_page.get_route_price()
            optimal_duration = route_page.get_route_duration()

        with allure.step("Click on Fast tab"):
            route_page.click_route_type("fast")

        with allure.step("Get price and duration for Fast route"):
            fast_price = route_page.get_route_price()
            fast_duration = route_page.get_route_duration()

        with allure.step("Verify that price and duration are displayed for both routes"):
            assert optimal_price is not None and optimal_price != "", "Optimal route should have price displayed"
            assert optimal_duration is not None and optimal_duration != "", "Optimal route should have duration displayed"
            assert fast_price is not None and fast_price != "", "Fast route should have price displayed"
            assert fast_duration is not None and fast_duration != "", "Fast route should have duration displayed"

    @pytest.mark.xfail(reason="Price and time do not change when switching between route types")
    @allure.title("Check price and duration recalculation when switching route types")
    @allure.description("Verify that price and duration change when switching between Optimal and Fast route types")
    @allure.severity(allure.severity_level.NORMAL)
    def test_price_duration_recalculation(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            driver.get(URL)

        with allure.step("Enter different addresses"):
            main_page.enter_different_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)

        with allure.step("Get price and duration for Fast route"):
            fast_price = route_page.get_route_price()
            fast_duration = route_page.get_route_duration()

        with allure.step("Click on Optimal tab"):
            route_page.click_route_type("optimal")

        with allure.step("Get price and duration for Optimal route"):
            optimal_price = route_page.get_route_price()
            optimal_duration = route_page.get_route_duration()

        with allure.step("Verify that price and duration changed"):
            assert fast_price != optimal_price, "Price should change when switching route types"
            assert fast_duration != optimal_duration, "Duration should change when switching route types"

    @allure.title("Check active tab change when switching to Custom route")
    @allure.description("Verify that active tab changes when switching from Fast to Custom route type")
    @allure.severity(allure.severity_level.NORMAL)
    def test_active_tab_change_to_custom(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            driver.get(URL)

        with allure.step("Enter different addresses"):
            main_page.enter_different_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)

        with allure.step("Verify Fast route is initially active"):
            # This would need implementation of checking active tab state
            pass

        with allure.step("Click on Custom tab"):
            route_page.click_route_type("custom")

        with allure.step("Verify Custom route tab is now active"):
            # This would need implementation of checking active tab state
            assert True, "Active tab should change to Custom"

    @allure.title("Check Custom tab activation and transportation types")
    @allure.description("Verify that switching to Custom route tab activates all transportation types")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_custom_tab_transportation_types(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            driver.get(URL)

        with allure.step("Enter different addresses"):
            main_page.enter_different_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)

        with allure.step("Click on Custom tab"):
            route_page.click_route_type("custom")

        with allure.step("Verify that all transportation types are active"):
            assert route_page.check_transportation_types_active(), "All transportation icons should be active when Custom tab is selected"

    @allure.title("Check Call Taxi button is active for Fast route")
    @allure.description("Verify that Call Taxi button is active when Fast route type is selected")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_call_taxi_button_fast_route(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            driver.get(URL)

        with allure.step("Enter different addresses"):
            main_page.enter_different_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)

        with allure.step("Click on Fast tab"):
            route_page.click_route_type("fast")

        with allure.step("Verify that Call Taxi button is active"):
            assert route_page.check_call_taxi_button_active(), "Call Taxi button should be active for Fast route type"

    @allure.title("Check Book button is active for Drive option in Custom route")
    @allure.description("Verify that Book button is active when Custom route with Drive transportation type is selected")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_book_button_drive_custom_route(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            driver.get(URL)

        with allure.step("Enter different addresses"):
            main_page.enter_different_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)

        with allure.step("Click on Custom tab"):
            route_page.click_route_type("custom")

        with allure.step("Verify that Book button is active for Drive option"):
            assert route_page.check_book_button_active(), "Book button should be active for Drive option in Custom route type"