from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com")

element = driver.find_element(By.NAME, "q")
element.clear()
element.send_keys("test skypro")
element.send_keys(Keys.RETURN)

sleep(4)

print(element)

driver.quit()