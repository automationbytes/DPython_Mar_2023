from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

from selenium.webdriver import ActionChains
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



driver.get("https://admin-demo.nopcommerce.com/Admin/Product/List")

driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//button[text()='Log in']").click()

pageSize = Select(driver.find_element(By.NAME,"products-grid_length"))
pageSize.select_by_visible_text("100")

time.sleep(5)
row = driver.find_elements(By.XPATH,'//table[@id="products-grid"]//tr')
rowsize = len(row)
print(rowsize)

col = driver.find_elements(By.XPATH,'//table[@id="products-grid"]//th')
colsize = len(col)
print(colsize)

map = {}
for j in range(1, colsize+1):
    header = driver.find_element(By.XPATH,f'//div[@class="dataTables_scrollHeadInner"]/table/thead//th[{j}]').get_attribute("textContent")
    print(header)
    map[header] = j
print(map)


for i in range(1, rowsize):
    product_name = driver.find_element(By.XPATH,f"//table[@id='products-grid']//tr[{i}]/td[{map['Product name']}]").text
    print(product_name)
    if product_name == "Windows 8 Pro":
        driver.find_element(By.XPATH,f"//table[@id='products-grid']//tr[{i}]/td[{map['Edit']}]/a").click()
        break