import pymysql
import numpy

conn=pymysql.connect('localhost','root','','test')

with conn:
    cur=conn.cursor()
    sql="SELECT * FROM app"
    cur.execute(sql)
    res=cur.fetchall()
    for row in res:
       print("{0} {1} {2} {3}".format(row[0], row[1], row[2],row[3]))
    print(cur.rowcount)   

for x  in range(2,10,3): print (x,end=" ")   
print("\n") 

lst=range(1,11)
lst_rev_9_5_2 = lst[9 : 4 : -2] 
print(lst_rev_9_5_2)