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
├── pages/           # Page Object classes
├── locators/        # Element locators
├── tests/           # Test modules
├── test_data.py     # Test data
├── conftest.py      # pytest configuration and fixtures
├── pytest.ini      # pytest settings
├── requirements.txt # Dependencies
└── .gitignore       # Git ignore rules
```

## Requirements

- Python 3.12+
- Google Chrome browser
- ChromeDriver (automatically managed by webdriver-manager)

## Setup and Running Tests

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_route_display.py

# Run with Allure report
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## Test Structure

Tests are organized into 4 main functional areas:

1. **test_route_display.py** - Route rendering functionality
2. **test_route_selection_block.py** - Route selection block rendering
3. **test_taxi_order_preparation.py** - Taxi order preparation
4. **test_taxi_order_full_flow.py** - Complete taxi ordering flow

Each test uses Page Object Model pattern for maintainable and readable code.