import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import unittest

@pytest.fixture(scope = 'class')
def prestep():   
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-infobars")

    options.add_argument("--start-maximized")
    options.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 2}
    )
    options.add_experimental_option(
        "prefs", {"profile.geolocation.default_content_setting'": 2}
    )
    driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(20)

    yield driver
    driver.close()
    print("Yield method called")

class TestWebSite:
    def test_google(self,prestep):
        driver = prestep
        driver.get("https://www.google.com/")
        print(driver.current_url)


    def test_bing(self,prestep):
        driver = prestep
        driver.get("https://www.bing.com/")
        print(driver.current_url)

    def test_yahoo(self,prestep):
        driver = prestep
        driver.get("https://www.yahoo.com/")
        print(driver.current_url)
