import boto3
from datetime import date
from os import environ
from datetime import date,timedelta
from os import environ
from configparser import ConfigParser

cp= ConfigParser()
cp.read( r"inputs.ini" )

ACCESS_KEY = 'AKIAQ4OTSXKAYQQVGGFP'
SECRET_KEY = cp.get('AWS','secret_key')
BUCKET=cp.get('AWS','bucketname')

campaign=input("Enter your campaign:")
if(campaign.lower()=='dcm'):
    localpath=cp.get('DCM','downloadpath')+'/DCMConnector.csv'
    filename="tapestryv2proddatawarehouse/delta/custom/email/custom_dcmphdfile_c0271afd195647ad83b9ae78a56a3dcb_"+date.today().strftime("%Y%m%d")+".csv"
    
elif(campaign.lower()=='kenshoo'):
    localpath=cp.get('Kenshoo','downloadpath')+'/KenshooConnector_2.csv'
    filename="tapestryv2proddatawarehouse/delta/custom/email/custom_dcmphdfile_c0271afd195647ad83b9ae78a56a3dcb_"+(date.today()-timedelta(1)).strftime("%Y%m%d")+".csv"
    
else:
   print("filename doesnt exists")

print(localpath)
s3=boto3.client('s3',aws_access_key_id=ACCESS_KEY , aws_secret_access_key=SECRET_KEY )
s3.download_file(BUCKET,filename,localpath)
