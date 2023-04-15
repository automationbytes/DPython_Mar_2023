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



driver.get("https://www.facebook.com/")

driver.find_element(By.ID,"email").send_keys("Tom")
driver.find_element(By.CLASS_NAME,"inputtext _55r1 _6luy _9npi").send_keys("Helo@1234")
#driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten pass").click()

'''
//tagname[@attribute = 'value']
//a[@data-testid="open-registration-form-button"]

//tagname[contains(@attribute,'val')]
//a[contains(@data-testid,"-registration-form-button")]

//tagname[@attribute1 = 'value' and @attribute2 = 'value' ]
//a[@role="button" and @data-testid="open-registration-form-button"]


//tagname[text()='value']
//button[text()='Log in']

'''