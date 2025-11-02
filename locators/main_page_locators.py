from selenium.webdriver.common.by import By


class MainPageLocators:
    # Address input fields
    FROM_FIELD = (By.XPATH, "//input[@id='from']")
    TO_FIELD = (By.XPATH, "//input[@id='to']")

    # Map route points
    A_POINT = (By.XPATH, "//ymaps[@class='ymaps-2-1-79-route-pin__label-a']")
    B_POINT = (By.XPATH, "//ymaps[@class='ymaps-2-1-79-route-pin__label-b']")