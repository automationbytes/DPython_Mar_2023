
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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



driver.get("https://www.redbus.in/")
driver.implicitly_wait(30)

driver.find_element(By.ID,"src").send_keys("Kol")
sourcedrpdwn = driver.find_elements(By.XPATH,'//input[@id="src"]/following-sibling::ul/li')

for s in sourcedrpdwn:
    print(s.text)
    if s.text == "Kollam":
        s.click()
        break


driver.find_element(By.ID,"onward_cal").click()
for i in range(12):
    monthtitle = driver.find_element(By.XPATH,'//td[@class="monthTitle"]').text
    print(monthtitle)

    if "Dec" in monthtitle:
        datecal = driver.find_elements(By.XPATH,'//table[@class="rb-monthTable first last"]//td')
        for d in datecal:    
            if d.text == "24":
                d.click()
                break
    else:
        driver.find_element(By.XPATH,'//td[@class="next"]/button').click()





# driver.close
# driver.quit