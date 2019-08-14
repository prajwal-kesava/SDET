import pymysql
import csv


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')

cur = conn.cursor()
with open("D:\\chr\\App.csv","r") as f:
    data=csv.reader(f)
    next(data)
    for row in data:
        sql="insert into app values("+'%s,'*(len(row)-1)+"%s)"
        print(sql)
        #cur.execute(sql,row)
conn.commit()
f.close()
'''
li=[]
for x in range(3):
    z="'{"+"{}".format(x)+"}',"
    li.append(z)
    if(x==2):
        y="'{"+"{}".format(x+1)+"}'"
        li.append(y)




p="".join(li)


with open("D:\\chr\\App.csv","r") as f:
    data=csv.reader(f)
    next(data)
    for row in data:
        sql="insert into app values("+'%s,'*(len(row)-1)+"%s)"
        ##print(sql)
        cur.execute(sql,row)
conn.commit()


''' 
sql="'INSERT INTO APP VALUES"+"("+p.format(row[0],row[1],row[2],row[3])+")'"
print(sql)
cur.execute(sql)
conn.commit()


'''
##Practice:

##cur.execute("CREATE TABLE APPP (ID INT(20) PRIMARY KEY,NAME VARCHAR(100),AGE INT(10),PHONE INT(100))")
sql="TRUNCATE TABLE APP"
cur.execute(sql)

head_rows=cur.fetchone()
print(len(head_rows))
rows=cur.fetchall()
for row in rows:
    print(row[0], row[1],row[2], row[3])

cur.close()
conn.close()
print("Done!")
'''