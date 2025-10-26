# URL and addresses
URL = 'https://ez-route.stand.praktikum-services.ru/'
FROM_ADDRESS = 'Хамовнический вал, 34'
TO_ADDRESS = 'Зубовский бульвар, 37'

# Taxi tariff names and descriptions
TAXI_TARIFF_DESCRIPTIONS = {
    "Рабочий": "Для деловых особ, которых отвлекают",
    "Сонный": "Для тех, кто не выспался",
    "Отпускной": "Если пришла пора отдохнуть",
    "Разговорчивый": "Если мысли не выходят из головы",
    "Утешительный": "Если хочется свернуться калачиком",
    "Глянцевый": "Если нужно блистать"
}

# Drive tariff descriptions
DRIVE_TARIFF_DESCRIPTIONS = {
    "Повседневный": "BMW 750 Просто по делам, ничего лишнего",
    "Походный": "KIA RIO Для путешествий",
    "Роскошный": "PORSCHE 911 Блеск, мощь, глянец"
}

# Expected text for same address route
SAME_ADDRESS_ROUTE_TEXT = {
    "cost": "Авто Бесплатно",
    "duration": "В пути 0 мин."
}

# Route types
ROUTE_TYPES = {
    "optimal": "Оптимальный",
    "fast": "Быстрый",
    "custom": "Свой"
}

# Transportation types
TRANSPORTATION_TYPES = {
    "car": "Машина",
    "walk": "Пешком",
    "taxi": "Такси",
    "bike": "Велосипед",
    "scooter": "Самокат",
    "drive": "Драйв"
}