from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    time.sleep(2)

    flash_message = driver.find_element(By.ID, "flash")
    print(flash_message.text.strip())

finally:
    driver.quit()