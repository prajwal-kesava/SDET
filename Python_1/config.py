from configparser import SafeConfigParser
from datetime import date,timedelta
cp= SafeConfigParser()
cp.read( r"inputs.ini" )
print(cp.sections())
print (cp.options('AWS'))
print(cp.get('DCM','downloadpath'))
localpath=cp.get('DCM','downloadpath')+'/DCMConnector.csv'

localpath2=cp.get('Kenshoo','downloadpath')+'/KenshooConnector.csv'
print(localpath2)
print(cp.get('AWS','access_key'))

filename="tapestryv2proddatawarehouse/delta/custom/email/custom_dcmphdfile_c0271afd195647ad83b9ae78a56a3dcb_"+date.today().strftime("%Y%m%d")+".csv"
print(filename)
print(' tapestryv2proddatawarehouse/delta/custom/email/custom_dcmphdfile_c0271afd195647ad83b9ae78a56a3dcb_20190702.csv')