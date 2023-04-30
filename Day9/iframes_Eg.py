from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
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



driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")

driver.implicitly_wait(20)

driver.find_element(By.CSS_SELECTOR,'a[title="Change Orientation"]').click()

driver.switch_to.frame("iframeResult")

driver.find_element(By.XPATH,"//button[text()='Try it']").click()

print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys("Devops")
driver.switch_to.alert.accept()


driver.switch_to.parent_frame()
driver.find_element(By.CSS_SELECTOR,'a[title="Change Orientation"]').click()
