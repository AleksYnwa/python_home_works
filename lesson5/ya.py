from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://ya.ru")

driver.get("https://vk.com")


driver.back()
driver.forward()
driver.refresh()
driver.set_window_size(1024, 768)

sleep(10)

driver.save_screenshot("./ya.png")