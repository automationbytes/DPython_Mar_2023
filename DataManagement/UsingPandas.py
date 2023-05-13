import pandas as pd

def readExcelwitPanda(rowname,colname):
    df = pd.read_excel("DPython_Mar_2023\\DataManagement\\Datasheet1.xlsx",sheet_name="DevopsUniv")
    val = df.loc[df['Label'] == rowname, colname].values[0]
    print(val)

readExcelwitPanda("OrangeHRM","Title")