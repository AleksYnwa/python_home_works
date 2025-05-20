from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

green_box = WebDriverWait(driver, 16).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success")))

print(green_box.text)

driver.quit()