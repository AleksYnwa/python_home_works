from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def make_screenshot(browser):
    browser.maximize_window()
    browser.get("https://ya.ru")
    sleep(3)

    browser.save_screenshot("./ya"+browser.name+".png")
    browser.quit()

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

make_screenshot(chrome)
make_screenshot(ff)
make_screenshot(edge)

