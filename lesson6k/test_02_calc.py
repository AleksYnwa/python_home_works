import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_slow_calculator_addition():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='7']").click()
        driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='+']").click()
        driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='8']").click()
        driver.find_element(By.XPATH, "//div[@class='keys']/span[text()='=']").click()

        result_locator = (By.CSS_SELECTOR, "div.screen")
        WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element(result_locator, "15"))

        result = driver.find_element(*result_locator).text
        assert result == "15", f"Ожидался результат '15', но получен '{result}'"

    finally:
        driver.quit()