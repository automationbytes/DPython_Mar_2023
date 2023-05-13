from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import unittest

class LaunchUrl(unittest.TestCase):
    def setUp(self):     
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
        self.driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def test_google(self):
        self.driver.get("https://www.google.com/")
        print(self.driver.current_url)

    
    def test_bing(self):
        self.driver.get("https://www.bing.com/")
        print(self.driver.current_url)

    def test_yahoo(self):
        self.driver.get("https://www.yahoo.com/")
        print(self.driver.current_url)


    def tearDown(self):
        pass
      #  self.driver.close()

if __name__ == "__main__":
    unittest.main()