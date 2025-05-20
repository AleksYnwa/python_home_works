from selenium.webdriver.common.by import By


class CartPage:
    def init(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()