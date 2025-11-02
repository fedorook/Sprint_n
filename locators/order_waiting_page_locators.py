from selenium.webdriver.common.by import By


class OrderWaitingPageLocators:
    # Waiting window elements
    SEARCH_CAR_TITLE = (By.XPATH, "//div[contains(text(),'Поиск машины')]")
    TIMER = (By.XPATH, "//div[@class='order-header-time']")
    CANCEL_BUTTON = (By.XPATH, "//button[@class='order-button']//img[@src='/static/media/plus.d25b8941.svg']")
    DETAILS_BUTTON = (By.XPATH, "//button[@class='order-button']//img[@src='/static/media/burger.7f0605c2.svg']")

    # Order completion elements
    ORDER_TITLE = (By.XPATH, "//div[@class='order-header-title']")
    CAR_NUMBER = (By.XPATH, "//div[@class='order-number']//div[@class='number']")
    CAR_IMAGE = (By.XPATH, "//div[@class='order-number']//img[@src='/static/media/economy.61e4a774.svg']")

    # Driver info
    DRIVER_NAME = (By.XPATH, "//div[@class='order-btn-group']//div[2]")
    DRIVER_AVATAR = (By.XPATH, "//img[@src='/static/media/bender.e90e5089.svg']")
    DRIVER_RATING = (By.XPATH, "//div[@class='order-button']//div[1]")

    # Scenario specific elements
    LAPTOP_TABLE_CHECKBOX = (By.XPATH, "//span[@class='slider round']")
    ORDER_REQUIREMENTS = (By.XPATH, "//div[contains(text(),'Требования к заказу')]")
    ORDER_NOW_BUTTON = (By.XPATH, "//button[@class='smart-button']")

    # Waiting window
    WAITING_WINDOW = (By.XPATH, "//div[@class='order-body']")