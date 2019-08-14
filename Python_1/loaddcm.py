import pandas as  pd 
import time
t2=time.time()
df=pd.read_csv("D:\\tapestryv2\\DCM\\DCMConnector.csv",skiprows=10)

df=df.astype({"Media Cost":'int64'})
print(df.dtypes)
if(df.dtypes[0]=="object"):
    print("Im")
  
t1=time.time()
print(f"{t1-t2}")
'''
def typist(typee):
    return typess[typee]

typess={
   'object':"sql+('\n\t%s VARCHAR(%s) ,' % (col[0],col[1]))"
}
print(typist('object'))

space=' ()'
under="___"
deltab=str.maketrans(space,under)
header="hello ()"
print(header.translate(deltab))
print(type(deltab))
ss="hello ()"
ss=ss.strip(")")
print(ss)
'''



