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



driver.get("https://demo.guru99.com/test/simple_context_menu.html")

driver.implicitly_wait(20)

actions = ActionChains(driver)

# actions.context_click(driver.find_element(By.XPATH,"//span[text()='right click me']")).click()
# actions.move_to_element(driver.find_element(By.XPATH,"//span[text()='Copy']"))
# actions.click(driver.find_element(By.XPATH,"//span[text()='Copy']"))
# actions.perform()


actions.double_click(driver.find_element(By.XPATH,"//span[text()='Double-Click Me To See Alert']")).click()
actions.perform()