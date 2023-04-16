
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

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


driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
driver.find_element(By.XPATH,'//a[@data-testid="open-registration-form-button"]').click()
driver.find_element(By.NAME,"firstname").send_keys("TOmmy")

driver.find_element(By.XPATH,"//label[text()='Custom']").click()

wait = WebDriverWait(driver,15)
wait.until(expected_conditions.element_to_be_clickable((By.NAME,"custom_gender")))
driver.find_element(By.NAME,"custom_gender").send_keys("Transgender")
