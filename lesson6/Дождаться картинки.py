from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

WebDriverWait(driver, 10).until(
        lambda d: len([img for img in d.find_elements(By.CSS_SELECTOR, "img")
                       if img.get_attribute("complete") == "true" and img.get_attribute("src")])
        >= 4
    )

images = driver.find_elements(By.CSS_SELECTOR, "img")

third_img_src = images[3].get_attribute("src")

print(third_img_src)

driver.quit()