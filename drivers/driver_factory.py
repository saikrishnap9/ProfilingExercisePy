# drivers/driver_factory.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os

class DriverFactory:
    def get_driver(self, browser: str):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            # You can add more options to the Chrome browser here.
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            # You can add more options to the Firefox browser here.
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            raise ValueError("Browser not supported")
        return driver
