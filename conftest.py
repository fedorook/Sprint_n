import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.taxi_order_page import TaxiOrderPage
from pages.order_waiting_page import OrderWaitingPage
from pages.order_details_page import OrderDetailsPage


# Browser fixture with setup and teardown
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=service)
    chrome.maximize_window()
    chrome.implicitly_wait(10)
    yield chrome
    chrome.quit()


# Fixture for main page (address input fields)
@pytest.fixture
def main_page(driver):
    return MainPage(driver)


# Fixture for route selection page
@pytest.fixture
def route_page(driver):
    return RoutePage(driver)


# Fixture for taxi order page
@pytest.fixture
def taxi_order_page(driver):
    return TaxiOrderPage(driver)


# Fixture for order waiting page
@pytest.fixture
def order_waiting_page(driver):
    return OrderWaitingPage(driver)


# Fixture for order details page
@pytest.fixture
def order_details_page(driver):
    return OrderDetailsPage(driver)