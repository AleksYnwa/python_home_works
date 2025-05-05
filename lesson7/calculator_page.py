from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CSS_SELECTOR, "div.screen")

        # Локаторы для кнопок
        self.button_locator = "//div[@class='keys']/span[text()='{}']"

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        return self

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))
        return self

    def click_button(self, button_text):
        locator = (By.XPATH, self.button_locator.format(button_text))
        self.driver.find_element(*locator).click()
        return self

    def perform_calculation(self, num1, operator, num2):
        self.click_button(num1)
        self.click_button(operator)
        self.click_button(num2)
        self.click_button('=')
        return self

    def get_result(self, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.screen, "15"))
        return self.driver.find_element(*self.screen).text