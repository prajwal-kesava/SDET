import pandas as pd
import json
import requests
from requests.auth import HTTPBasicAuth
from configparser import ConfigParser
from pandas.io.json import json_normalize
cp= ConfigParser()
cp.read( r"jiraprop.ini" )
API_END_URL=input("Enter ur url here: ")

JIRA_EMAIL = cp.get('user details','user')
JIRA_TOKEN = cp.get('user details','apikey')
BASE_URL = cp.get('user details','server')
API_URL = "/rest/api/3/"+API_END_URL
API_URL = BASE_URL+API_URL
print(API_URL)
BASIC_AUTH = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)
HEADERS = {'Content-Type' : 'application/json;charset=iso-8859-1'}
def api_call(url,header,authentication):
    response = requests.get(
    url,
    headers=header,
    auth=authentication
    )
    return response.text
respone_data=api_call(API_URL,HEADERS,BASIC_AUTH)
data=json.loads(respone_data)
print(type(data))
JSON_FILE=input('Enter the file name :')
with open("json data/"+JSON_FILE+".json",'w',encoding='utf-8') as f:
	json.dump(data, f, ensure_ascii=False, indent=4)

with open("json data/"+JSON_FILE+".json") as f:
    d=json.load(f)

meta_data=[]
record_data=''

print(type(d))
if(type(d)==list):
    for li in d:
        for key,value in li.items():
            if(isinstance(value,list)):
                record_data=key
            else:
                meta_data.append(key)
               
elif(type(d)==dict):
    for key,value in d.items():
        if(isinstance(value,list)):
            record_data=key
        else:
            meta_data.append(key)

print(meta_data,record_data)  
#for subtasks
if record_data=='':
    record_data=None
work_data=json_normalize(data=d,errors='ignore',sep='_')
# work_2=json_normalize(data=work_data,record_path='issueTypes',record_prefix='issueTypes',sep='_')
# works_data1 = json_normalize(data=d['issues'],record_path=['issues',[fields','subtasks']],record_prefix='subtasks_',meta_prefix='issues_',meta='id',sep="_")
# works_data2 = json_normalize(data=d['issues'],record_path=['fields','fixVersions'],record_prefix='fixVersions',meta_prefix='issues_',meta='id',sep="_")
# works_data=pd.merge(works_data1,works_data2,on='issues_id',how='left')

# record_pref=record_data+"_"

# print(works_data1.head(5))
# df_row_merged = pd.concat([df_a, df_b], ignore_index=True)
# print(works_data.head(5))
work_data.to_csv("jira data/"+JSON_FILE+'.csv')

for i in range(len(d)):
    API_END_URL_2=API_URL+"/"+d[i]['key']
    print(API_END_URL_2)
    response_data=api_call(API_END_URL_2,HEADERS,BASIC_AUTH)
    data=json.loads(response_data)
    print(type(d))
    with open("json data/project_"+str(i)+".json",'w',encoding='utf-8') as f:
	    json.dump(data, f, ensure_ascii=False, indent=4)

    with open("json data/project_"+str(i)+".json",'r') as f:
        data=json.load(f)
    work_transform=work_data+str(i)
    work_data=work_transform=json_normalize(data,errors='ignore',sep='_')
    work_data.to_csv("jira data/project_"+str(i)+".csv")





