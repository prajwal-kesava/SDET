li=[]
for x in range(3):
    z="{"+"{}".format(x)+"},"
    li.append(z)
    if(x==2):
        y="{"+"{}".format(x+1)+"}"
        li.append(y)

print(li,end="\n")


p="".join(li)
print(p)

print("insert into app values("+'%s,'*4+"%s)")
sql="create table dcm("+'{0},{1}'.format('hi','hello')+")"
print(sql)