from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

button = driver.find_element(By.ID, "updatingButton").click()

WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))

updated_button = driver.find_element(By.ID, "updatingButton")
print(updated_button.text)

driver.quit()

