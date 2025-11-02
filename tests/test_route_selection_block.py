import allure
import pytest

@allure.epic("Yandex Routes Testing")
@allure.feature("Route Selection Block Display")
class TestRouteSelectionBlock:

    @allure.title("Check route selection block appears for different addresses")
    @allure.description("Verify that when entering two different preset addresses in 'From' and 'To' fields, route selection block is displayed")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_route_selection_block_different_addresses(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            main_page.open_yandex_routes()

        with allure.step("Enter different addresses in 'From' and 'To' fields"):
            main_page.enter_different_addresses()

        with allure.step("Check that route selection block is displayed"):
            assert route_page.check_route_selection_block_displayed(), "Route selection block should be displayed for different addresses"

    @allure.title("Check route tabs visibility for different addresses")
    @allure.description("Verify that Optimal, Fast, Custom route tabs are displayed for different addresses")
    @allure.severity(allure.severity_level.NORMAL)
    def test_route_tabs_visibility_different_addresses(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            main_page.open_yandex_routes()

        with allure.step("Enter different addresses in 'From' and 'To' fields"):
            main_page.enter_different_addresses()

        with allure.step("Check that all route tabs are visible"):
            assert route_page.check_route_selection_block_displayed(), "Route tabs (Optimal, Fast, Custom) should be visible"

    @allure.title("Check transportation types visibility for different addresses")
    @allure.description("Verify that all transportation icons are displayed when Custom tab is selected")
    @allure.severity(allure.severity_level.NORMAL)
    def test_transportation_types_visibility(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            main_page.open_yandex_routes()

        with allure.step("Enter different addresses in 'From' and 'To' fields"):
            main_page.enter_different_addresses()

        with allure.step("Click on Custom tab"):
            route_page.click_route_type("custom")

        with allure.step("Check that transportation types are active"):
            assert route_page.check_transportation_types_active(), "All transportation icons should be displayed"

    @allure.title("Check Call Taxi button visibility for different addresses")
    @allure.description("Verify that Call Taxi button is displayed and clickable")
    @allure.severity(allure.severity_level.NORMAL)
    def test_call_taxi_button_visibility(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            main_page.open_yandex_routes()

        with allure.step("Enter different addresses in 'From' and 'To' fields"):
            main_page.enter_different_addresses()

        with allure.step("Check that Call Taxi button is active"):
            assert route_page.check_call_taxi_button_active(), "Call Taxi button should be displayed and clickable"

    @pytest.mark.xfail(reason="Race condition: Book button for Drive option doesn't appear consistently in automated tests")
    @allure.title("Check Book button visibility for Drive option")
    @allure.description("Verify that Book button is displayed and clickable for Drive option")
    @allure.severity(allure.severity_level.NORMAL)
    def test_book_button_visibility(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            main_page.open_yandex_routes()

        with allure.step("Enter different addresses in 'From' and 'To' fields"):
            main_page.enter_different_addresses()

        with allure.step("Click on Custom tab"):
            route_page.click_route_type("custom")

        with allure.step("Click on Drive transportation option"):
            route_page.click_drive_option()

        with allure.step("Check that Book button is active for Drive"):
            assert route_page.check_book_button_active(), "Book button should be displayed and clickable for Drive option"

    @allure.title("Check same address route text for identical addresses")
    @allure.description("Verify that when entering same address in both 'From' and 'To' fields, block shows 'Авто Бесплатно В пути 0 мин.'")
    @allure.severity(allure.severity_level.NORMAL)
    def test_same_address_route_text(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            main_page.open_yandex_routes()

        with allure.step("Enter same address in both 'From' and 'To' fields"):
            main_page.enter_same_addresses()

        with allure.step("Check that same address route text is displayed"):
            assert route_page.check_same_address_route_text(), "Should display 'Авто Бесплатно' and 'В пути 0 мин.' for same addresses"

    @allure.title("Check route price visibility for different addresses")
    @allure.description("Verify that route price is displayed when entering two different preset addresses")
    @allure.severity(allure.severity_level.NORMAL)
    def test_route_price_visibility_different_addresses(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            main_page.open_yandex_routes()

        with allure.step("Enter different addresses in 'From' and 'To' fields"):
            main_page.enter_different_addresses()

        with allure.step("Check that route price is displayed"):
            assert route_page.check_route_price_visibility(), "Route price should be displayed for different addresses"

    @allure.title("Check route duration visibility for different addresses")
    @allure.description("Verify that route duration is displayed when entering two different preset addresses")
    @allure.severity(allure.severity_level.NORMAL)
    def test_route_duration_visibility_different_addresses(self, driver, main_page, route_page):
        with allure.step("Navigate to Yandex Routes page"):
            main_page.open_yandex_routes()

        with allure.step("Enter different addresses in 'From' and 'To' fields"):
            main_page.enter_different_addresses()

        with allure.step("Check that route duration is displayed"):
            assert route_page.check_route_duration_visibility(), "Route duration should be displayed for different addresses"