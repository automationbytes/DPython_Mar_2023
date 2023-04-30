from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
import time
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



driver.get("https://www.openmultipleurl.com/")

driver.implicitly_wait(20)

driver.find_element(By.ID,"list_urls").send_keys("https://www.google.com/")
driver.find_element(By.ID,"list_urls").send_keys(Keys.ENTER)


driver.find_element(By.ID,"list_urls").send_keys("https://www.bing.com/")
driver.find_element(By.ID,"list_urls").send_keys(Keys.ENTER)


driver.find_element(By.ID,"list_urls").send_keys("https://www.amazon.com/")
driver.find_element(By.ID,"list_urls").send_keys(Keys.ENTER)


driver.find_element(By.ID,"list_urls").send_keys("https://www.microsoft.com/")
driver.find_element(By.ID,"list_urls").send_keys(Keys.ENTER)


driver.find_element(By.ID,"list_urls").send_keys("https://www.apple.com/")
driver.find_element(By.ID,"list_urls").send_keys(Keys.ENTER)

driver.find_element(By.CSS_SELECTOR,'input[value="Go Now"]').click()

parentwindow = driver.current_window_handle
print(parentwindow)

allopenwindows = driver.window_handles #this include parent window also
print(allopenwindows)

for a in allopenwindows:
    if a!= parentwindow:
        time.sleep(5)
        driver.switch_to.window(a)
        print(driver.current_url)

        if 'google' in driver.current_url:
            driver.find_element(By.XPATH,'//textarea[@maxlength="2048"]').send_keys("Hello")
            driver.find_element(By.XPATH,'//textarea[@maxlength="2048"]').send_keys(Keys.ENTER)
        else:
            driver.close()
            