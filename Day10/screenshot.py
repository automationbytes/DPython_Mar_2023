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



driver.get("https://redbus.in/")

driver.implicitly_wait(20)

import time
import datetime
import calendar
curtimr = datetime.datetime.now()
timeformater = str(curtimr).replace(" ","").replace(":","-").replace(".","-")
print(timeformater)

driver.save_screenshot("DPython_Mar_2023\\Day10\\redbus_"+timeformater+".png")

driver.get_screenshot_as_file("DPython_Mar_2023\\Day10\\redbus_file"+timeformater+".png")


import os
print(os.getcwd())
driver.save_screenshot(os.getcwd()+"\\DPython_Mar_2023\\Day10\\redbus_cwd"+timeformater+".png")

driver.get_screenshot_as_file(os.getcwd()+"\\DPython_Mar_2023\\Day10\\redbus_file_cwd"+timeformater+".png")
