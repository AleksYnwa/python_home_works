import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_slow_calculator_addition():
    # Инициализация драйвера
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        # Использование Page Object
        calculator = CalculatorPage(driver)
        (calculator.open()
         .set_delay(45)
         .perform_calculation('7', '+', '8'))

        # Проверка результата
        result = calculator.get_result()
        assert result == "15", f"Expected '15', but got '{result}'"

    finally:
        driver.quit()