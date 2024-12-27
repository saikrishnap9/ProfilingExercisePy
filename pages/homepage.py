# pages/homepage.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from configs.settings import BASE_URL

class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = BASE_URL

    def open(self):
        self.driver.get(self.url)

    def get_page_title(self):
        return self.driver.title
    
    def get_title_text(self):
        return self.driver.find_element(By.XPATH, f"//div[@class='login_logo']").text
    
    def login(self):
        self.driver.find_element(By.XPATH, f"//input[@name='user-name']").send_keys("standard_user")
        self.driver.find_element(By.XPATH, f"//input[@name='password']").send_keys("secret_sauce")
        self.driver.find_element(By.XPATH, f"//input[@name='login-button']").click()

    def add_item_to_cart(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//button[@name='add-to-cart-sauce-labs-backpack']").click()
        
    def get_cart_item(self):
        self.driver.find_element(By.XPATH, f"//a[@class='shopping_cart_link']").click()
        time.sleep(2)
        return self.driver.find_element(By.XPATH,f"//div[text()='Sauce Labs Backpack']").is_displayed()
        
    def click_logout(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,f"//button[@id='react-burger-menu-btn']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,f"//a[@id='logout_sidebar_link']").click()

        