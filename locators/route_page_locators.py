from selenium.webdriver.common.by import By


class RoutePageLocators:
    # Address input fields
    FROM_FIELD = (By.XPATH, "//input[@id='from']")
    TO_FIELD = (By.XPATH, "//input[@id='to']")

    # Route types
    OPTIMAL_TAB = (By.XPATH, "//div[contains(text(),'Оптимальный')]")
    FAST_TAB = (By.XPATH, "//div[contains(text(),'Быстрый')]")
    CUSTOM_TAB = (By.XPATH, "//div[contains(text(),'Свой')]")

    # Transportation icons
    CAR_ICON = (By.XPATH, "//img[@src='/static/media/car.8a2b1ff5.svg']")
    WALK_ICON = (By.XPATH, "//img[@src='/static/media/walk.d33bf83c.svg']")
    TAXI_ICON_ACTIVE = (By.XPATH, "//img[@src='/static/media/taxi-active.b0be3054.svg']")
    BIKE_ICON = (By.XPATH, "//img[@src='/static/media/bike.fb41c762.svg']")
    SCOOTER_ICON = (By.XPATH, "//img[@src='/static/media/scooter.cf9bb57e.svg']")
    DRIVE_ICON = (By.XPATH, "//img[@src='/static/media/drive.fa5137d7.svg']")

    # Route info
    PRICE = (By.XPATH, "//div[@class='text']")
    DURATION = (By.XPATH, "//div[@class='duration']")

    # Action buttons
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(),'Вызвать такси')]")
    BOOK_BUTTON = (By.XPATH, "//button[contains(text(),'Забронировать')]")

    # Same address route text
    FREE_AUTO_TEXT = (By.XPATH, "//div[contains(text(),'Авто Бесплатно')]")
    ZERO_MINUTES_TEXT = (By.XPATH, "//div[contains(text(),'В пути 0 мин.')]")