import pandas as pd


excel_url = 'https://github.com/lutherjohn/Excel-Dummy/blob/master/student.xlsx?raw=true'
csv_url   = 'https://github.com/lutherjohn/Excel-Dummy/blob/master/student.csv?raw=true'

#url = 'https://github.com/lutherjohn/Excel-Dummy/blob/master/student.xlsx?raw=true'
#at the end of the file extention of your excel file or csv ex: sample.xlsx?raw=true, sample.csv?raw=true

excel_df = pd.read_excel(excel_url)
excel = excel_df.head(3)

df = pd.read_csv(csv_url)
w = df.head(3)

print(excel)
