# зайти на лабиринт
# найти книги по слову Python
# собрать все карточки товаров
# вывести в консоль информацию: название, автор, цена


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.labirint.ru/")

search_locator = "#search-field"

driver.find

sleep(5)
