from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ActionChains

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



driver.get("https://www.snapdeal.com/")

driver.implicitly_wait(20)

driver.execute_script("arguments[0].click();",driver.find_element(By.XPATH,"//span[text()='Mattresses']"))
