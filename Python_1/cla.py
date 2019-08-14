import csv, os, string, sys
import pymysql
import pandas as  pd 
import numpy as np
import time
t0=time.time()
if len(sys.argv)<2:
	print("\nUsage: csv2tbl.py path/datafile.csv (0,1,2,3 = column name format):")
	print ("\nFormat: 0 = TitleCasedWords")
	print ("        1 = Titlecased_Words_Underscored")
	print ("        2 = lowercase_words_underscored")
	print ("        3 = Words_underscored_only (leave case as in source)")
	sys.exit()
else:
	if len(sys.argv)==2:
		dummy, datafile,namefmt = '0'
	else: dummy, datafile, namefmt = sys.argv

namefmt = int(namefmt)
#outfile = os.path.basename(datafile)
tblname = os.path.basename(datafile).split('.')[0]
outfile = os.path.dirname(datafile) + '\\' + tblname + '.sql'

# Create string translation tables
allowed = ' _01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
delchars = ''
for i in range(255):
	if chr(i) not in allowed: delchars = delchars + chr(i)
        
deltable =str.maketrans(' ()','___')
print(deltable)
print(datafile)
# Create list of column [names],[widths]

reader = csv.reader(open(datafile))
for x in range(10):  # skip the first 500 rows
    next(reader)
    
row = next(reader)

print(row)
nc = len(row)
print(nc)
cols = []
for col in row:
	print(col,end=" ")
	col = col.strip()
	col = col.translate(deltable)
	fmtcol = col
	if namefmt < 3:
		# Title case individual words, leaving original upper chars in place
		fmtcol = ''
		for i in range(len(col)):
			if col.title()[i].isupper(): fmtcol = fmtcol + col[i].upper()
			else: fmtcol = fmtcol + col[i]
	if namefmt == 2: fmtcol = col.lower()
	if namefmt == 0: fmtcol =fmtcol.translate(deltable)   # Remove underscores
	
	d = 0
	dupcol = fmtcol	
	while dupcol in cols:
		d = d + 1
		dupcol = fmtcol + '_' + str(d)
	cols.append([dupcol,1])

# Determine max width of each column in each row
rc = 0
for row in reader:
	rc = rc + 1
	if len(row) == nc:
		for i in range(len(row)):
			fld = str.strip(row[i])
			if len(fld) > cols[i][1]:
				cols[i][1] = len(fld)
	else: print('Warning: Line %s ignored. Different width than header' % (rc))

print("\n")

df=pd.read_csv(datafile,skiprows=10)
print(df.head())

sql = f'CREATE TABLE {tblname}(' 
'''
def typist(typee):
    return typess[typee]

typess={
   'object':sql+('\n\t%s VARCHAR(%s) ,' % (col[0],col[1])),'float':sql+('\n\t%s FLOAT(9,5) ,' % (col[0])),'int64':sql + ('\n\t%s INT(%s) ,' % (col[0],col[1]))
}
'''
x=int(0)
if (x in range(len(row)-1)):
    for col in cols:
        if(df.dtypes[x]=='object'):
            sql = sql+ f"\n\t{col[0]} VARCHAR({col[1]}),"
            x=x+1
        elif(df.dtypes[x]=='int64'):
            sql = sql + f"\n\t{col[0]} INT({col[1]}),"
            x=x+1
        elif(df.dtypes[x]=='float'):
            #sql = sql+('\n\t%s FLOAT(%s,5) ,' % (col[0]),col[1])
            sql=sql+f"\n\t{col[0]} Float({col[1]},5),"
            x=x+1
        
sql = sql[:len(sql)-1] + '\n)'
print(sql)


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')

cur = conn.cursor()
cur.execute(sql)
conn.commit()

with open(datafile,"r") as f:
    data=csv.reader(f)
    for x in range(10):  # skip the first 10 rows
        next(data)

    next(data)
    for row in data:
        sql="insert into "+tblname+" values("+'%s,'*(len(row)-1)+"%s)"
        ##print(sql)
        cur.execute(sql,row)
conn.commit()
f.close()

sqlfile = open(outfile,'w')
sqlfile.write(sql)
sqlfile.close

print('%s created.' % (outfile))
t1=time.time()
print("Compiled time :"+f"{t1-t0}")