import configparser

config = configparser.ConfigParser()
config.read("DPython_Mar_2023\\DataManagement\\config.ini")

value = config.get('userdetails',"url")
print(value)

config.add_section("Selenium")
config.set("Selenium","Timeout","20")
config.set("Selenium","Browser","Chrome")

with open("DPython_Mar_2023\\DataManagement\\config.ini","w")as f:
    config.write(f)
