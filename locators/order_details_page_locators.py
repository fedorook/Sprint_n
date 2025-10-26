from selenium.webdriver.common.by import By


class OrderDetailsPageLocators:
    # Price elements
    TARIFF_PRICE = (By.XPATH, "//div[@class='tcard-price']")
    PRICE_IN_DETAILS = (By.XPATH, "//div[contains(text(),'Стоимость')]")

    # Details window elements
    PICKUP_ADDRESS = (By.XPATH, "//div[contains(text(),'Адрес подачи')]")
    DESTINATION_ADDRESS = (By.XPATH, "//div[contains(text(),'Адрес назначения')]")
    PAYMENT_METHOD = (By.XPATH, "//div[contains(text(),'Способ оплаты')]")

    # Trip info section
    TRIP_INFO_TITLE = (By.XPATH, "//div[contains(text(),'Еще про поездку')]")
    COST_INFO = (By.XPATH, "//div[contains(text(),'Стоимость')]")

    # Buttons
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(),'Отменить')]")
    DETAILS_BUTTON = (By.XPATH, "//button[contains(text(),'Детали')]")