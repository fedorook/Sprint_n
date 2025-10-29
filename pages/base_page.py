import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from test_data import FROM_ADDRESS, TO_ADDRESS


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Navigate to URL")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Find element with wait")
    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Wait for elements to appear")
    def wait_for_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Check if element is clickable")
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    @allure.step("Click element")
    def click_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step("Check if element is displayed")
    def is_element_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except:
            return False

    @allure.step("Check if element is not visible")
    def wait_for_element_to_disappear(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    @allure.step("Check if text appears in element")
    def wait_for_text_in_element(self, locator, text):
        return WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Add text to element")
    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Get text from element")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Scroll to element")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Enter different addresses")
    def enter_different_addresses(self, from_locator, to_locator):
        self.add_text_to_element(from_locator, FROM_ADDRESS)
        self.add_text_to_element(to_locator, TO_ADDRESS)

    @allure.step("Enter same addresses")
    def enter_same_addresses(self, from_locator, to_locator):
        self.add_text_to_element(from_locator, FROM_ADDRESS)
        self.add_text_to_element(to_locator, FROM_ADDRESS)

    @allure.step("Hover over element")
    def hover_over_element(self, locator):
        element = self.find_element_with_wait(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step("Wait for element with extended timeout")
    def wait_for_element_extended(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))