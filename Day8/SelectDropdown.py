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



driver.get("https://admin-demo.nopcommerce.com/Admin/Order/List")
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//button[text()='Log in']").click()

countrylist = driver.find_element(By.ID,"BillingCountryId")
#countrydropdown = Select(driver.find_element(By.ID,"BillingCountryId"))
countrydropdown = Select(countrylist)

#countrydropdown.select_by_value("73")
#countrydropdown.select_by_visible_text("Sweden")
countrydropdown.select_by_index(11)

for c in countrydropdown.options:
    print(c.get_attribute("value"),c.text)
    if c.text == "Somalia":
        c.click()
        break

    


'''
By 3 ways we can select the values from dropdown

1) Select By value
2) Select by Visible text
3) Select by index

'''