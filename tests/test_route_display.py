import allure
from test_data import URL
from locators.main_page_locators import MainPageLocators


@allure.epic("Yandex Routes Testing")
@allure.feature("Route Display")
class TestRouteDisplay:

    @allure.title("Check route points visibility after entering different addresses")
    @allure.description("Verify that when entering two different preset addresses in 'From' and 'To' fields, two route points are displayed on the map")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_route_points_visibility(self, driver, main_page):
        with allure.step("Navigate to Yandex Routes page"):
            driver.get(URL)

        with allure.step("Enter different addresses in 'From' and 'To' fields"):
            main_page.enter_different_addresses(MainPageLocators.FROM_FIELD, MainPageLocators.TO_FIELD)

        with allure.step("Check that route points A and B are displayed on the map"):
            assert main_page.check_route_points_displayed(), "Route start and end points should be visible on the map"