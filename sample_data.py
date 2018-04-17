import pandas as pd


excel_url = 'https://github.com/lutherjohn/Excel-Dummy/blob/master/student.xlsx?raw=true'
csv_url   = 'https://github.com/lutherjohn/Excel-Dummy/blob/master/student.csv?raw=true'

#url = 'https://github.com/lutherjohn/Excel-Dummy/blob/master/student.xlsx?raw=true'
#at the end of the file extention of your excel file or csv set the raw to true for python to read the files from github repo.
#ex: sample.xlsx?raw=true, sample.csv?raw=true

excel_df = pd.read_excel(excel_url)
excel = excel_df.head(3)

csv_df = pd.read_csv(csv_url)
csv = csv_df.head(4)

print(csv)
#print(excel)
