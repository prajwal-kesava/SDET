import csv
import pandas as pd 
import numpy as np
import os
from datetime import date
header=[]
data=pd.read_csv("D:\\tapestryv2\\DCM\\DCMConnector.csv",skiprows=10)
data['new1']=date.today().strftime("%Y-%m-%d")
header=list(data)
print(header[0])
print(len(list(data)))
print(data.head())
for x in range(len(header)):
    print(f"Im in {header[x]}")
 
'''
for row in data:
    print(row)
data['new1']=""
print(data.head())
data.to_csv("D:\\tapestryv2\\Kenshoo\\KENSHOO3.csv",index=None)
print("csv created")
'''
data.to_csv("D:\\tapestryv2\\DCM\\DCMConnector3.csv",index=False)
