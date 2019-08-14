import pandas as pd
import xlrd
pd.read_excel('D:\chr\Hello11.xlsx',sheetname=1).to_csv('D:\chr\Test1.csv', index=False)

excel_name='D:\chr\Hello11.xlsx'
movies=pd.read_excel(excel_name)
print(movies)