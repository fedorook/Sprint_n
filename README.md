# Sprint_n - Yandex.Routes Project

Automated tests for the educational service "Yandex.Routes" as part of QA Automation Engineer (Python Extended) course from Yandex Practicum.

## Project Description

This project contains automated tests for testing the functionality of the "Yandex.Routes" web application. The tests cover main user scenarios:

- Route rendering on map
- Route selection block rendering
- Taxi order preparation
- Taxi tariff ordering (full flow)

## Technologies

- **Selenium WebDriver** - for browser automation
- **pytest** - testing framework
- **Allure** - for report generation
- **Page Object Model** - code organization pattern

## Project Structure

```
Sprint_n/
├── pages/          # Page Object classes
├── test/           # Test modules
├── test_data.py    # Test data
├── conftest.py     # pytest configuration
├── pytest.ini     # pytest settings
└── requirements.txt # Dependencies
```

## Running Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run with Allure report
pytest --alluredir=allure-results
allure serve allure-results
```