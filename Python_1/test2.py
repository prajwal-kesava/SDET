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

BASIC_AUTH = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)
HEADERS = {'Content-Type' : 'application/json;charset=iso-8859-1'}

response = requests.get(
API_URL,
headers=HEADERS,
auth=BASIC_AUTH
)

data=json.loads(response.text)
#print(data)
JSON_FILE=input('Enter the file name :')
with open("json data/"+JSON_FILE+".json",'w',encoding='utf-8') as f:
	json.dump(data, f, ensure_ascii=False, indent=4)

with open("json data/"+JSON_FILE+".json") as f:
    d=json.load(f)

meta_data=[]
record_data=''

print(type(d))
# if(type(d)==dict):
#     for li in d:
#         for key,value in li.items():
#             if(isinstance(value,(list,dict))):
#                 record_data=key
#             else:
#                 meta_data.append(key)
#     works_data = json_normalize(data=d,sep="_")            

# for key,value in d.items:
#     if(isinstance(value,(list,dict))):
#             record_data=key
#     else:
#         meta_data.append(key)

print(meta_data,record_data)  
#for subtasks
fix= json_normalize(data=d,record_path=['issues',['fields','fixVersions']],sep="_")
sub=json_normalize(data=d,record_path=['issues',['fields','subtasks']],sep="_")

work_data=pd.concat([fix,sub],sort=True)
# record_pref=record_data+"_"

# print(works_data.head(5))

work_data.to_csv("jira data/"+JSON_FILE+'.csv')

