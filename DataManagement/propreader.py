import configparser
config = configparser.ConfigParser()
config.read("DPython_Mar_2023\\DataManagement\\config.properties")
print(config['userdetails']['user'])

config['selenium'] = {'timeout':'30',"browser":"chrome"}
with open("DPython_Mar_2023\\DataManagement\\config.properties","w")as f:
    config.write(f)