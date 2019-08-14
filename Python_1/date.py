from datetime import datetime,date,timedelta
from os import environ
print(  (date.today()-timedelta(1)).strftime("%Y%m%d"))
print( datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d'))
filename="tapestryv2proddatawarehouse/delta/custom/email/custom_dcmphdfile_c0271afd195647ad83b9ae78a56a3dcb_"+(date.today()-timedelta(1)).strftime("%Y%m%d")+".csv"
print(filename)
path=""
print(path)

print(environ.get('HOMEPATH'))