import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_shop_checkout():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        product_ids = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        for product_id in product_ids:
            wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Aleksandr")
        driver.find_element(By.ID, "last-name").send_keys("Stolovich")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        total_elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        total_text = total_elem.text  # e.g., 'Total: $58.29'
        total_amount = total_text.split("$")[1]

        assert total_amount == "58.29", f"Expected total to be $58.29 but got ${total_amount}"

    finally:
        driver.quit()