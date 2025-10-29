from selenium.webdriver.common.by import By


class TaxiOrderPageLocators:
    # Address fields
    FROM_FIELD = (By.XPATH, "//input[@id='from']")
    TO_FIELD = (By.XPATH, "//input[@id='to']")

    # Taxi tariffs
    WORKING_TARIFF = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Рабочий')]")
    SLEEPY_TARIFF = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Сонный')]")
    VACATION_TARIFF = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Отпускной')]")
    TALKATIVE_TARIFF = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Разговорчивый')]")
    CONSOLATION_TARIFF = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Утешительный')]")
    GLOSSY_TARIFF = (By.XPATH, "//div[@class='tcard-title'][contains(text(),'Глянцевый')]")

    # All tariff cards
    ALL_TARIFF_CARDS = (By.XPATH, "//div[@class='tariff-cards']//div[contains(@class,'tcard')]")

    # Tariff info button
    TARIFF_INFO_BUTTON = (By.XPATH, "//div[@class='tcard active']//button[@class='i-button tcard-i active']")
    TARIFF_DESCRIPTION = (By.XPATH, "//div[@class='tcard active']//div[@class='i-floating']//div[@class='i-dPrefix']")

    # Order form fields
    PHONE_FIELD = (By.XPATH, "//div[contains(text(),'Телефон')]")
    PAYMENT_METHOD_FIELD = (By.XPATH, "//div[@class='pp-text'][contains(text(),'Способ оплаты')]")
    COMMENT_FIELD = (By.XPATH, "//label[contains(text(),'Комментарий водителю...')]")
    ORDER_REQUIREMENTS_FIELD = (By.XPATH, "//div[contains(text(),'Требования к заказу')]")

    # Order button
    ORDER_BUTTON = (By.XPATH, "//span[contains(text(),'Ввести номер и заказать')]")

    # Route info
    ROUTE_INFO = (By.XPATH, "//span[contains(text(),'Маршрут составит 3 км. и займёт 3 мин.')]")

    # Call taxi button
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(),'Вызвать такси')]")