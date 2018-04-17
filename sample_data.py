import pandas as pd


url = 'https://github.com/lutherjohn/Excel-Dummy/blob/master/student.xlsx?raw=true'


df = pd.read_excel(url,sheetname=0,header=1)
w = df.head(5)

print(w)
