# tests/test_homepage.py

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from drivers.driver_factory import DriverFactory
from pages.homepage import HomePage
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    # Setup browser driver
    driver_factory = DriverFactory()
    driver = driver_factory.get_driver("chrome")  # Or you can use "firefox"
    yield driver
    driver.quit()  # Teardown: Close the browser after the test

def test_homepage_title(driver: WebDriver | WebDriver):
    homepage = HomePage(driver)
    homepage.open()
    title = homepage.get_page_title()
    assert title == "Swag Labs", f"Expected 'Swag Labs', but got {title}"
    assert homepage.get_title_text()=="Swag Labs", f"Expected 'Swag Labs'"
    homepage.login()
    homepage.add_item_to_cart()
    assert homepage.get_cart_item()==True,"item not verified"
    homepage.click_logout()

