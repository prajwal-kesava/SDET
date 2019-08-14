import pandas as pd
import json
import requests
from requests.auth import HTTPBasicAuth
from configparser import ConfigParser
from pandas.io.json import json_normalize
cp= ConfigParser()
cp.read( r"jiraprop.ini" )

JIRA_EMAIL = cp.get('user details','user')
JIRA_TOKEN = cp.get('user details','apikey')
BASE_URL = cp.get('user details','server')
API_URL = "/rest/api/3/project/SR/statuses"

API_URL = BASE_URL+API_URL

BASIC_AUTH = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)
HEADERS = {'Content-Type' : 'application/json;charset=iso-8859-1'}

response = requests.get(
API_URL,
headers=HEADERS,
auth=BASIC_AUTH
)

data=json.loads(response.text)

print(data)

#Loading  response into file 
with open("data.json",'w',encoding='utf-8') as f:
	json.dump(data, f, ensure_ascii=False, indent=4)


#json normalize method
with open('data.json') as f:
    d=json.load(f)

   
'''
works_data = json_normalize(d,record_path=['self','id','name','subtask',meta="statuses",errors='ignore')

print(works_data.head(5))
'''
result = json_normalize(d, record_path='statuses', errors='ignore',record_prefix='statuses_',meta=['self','id','name','subtask'],meta_prefix=None)
print(result)
result.to_csv('pan.csv')

