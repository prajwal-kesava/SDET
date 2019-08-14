from jira import JIRA
import pymysql
from configparser import ConfigParser
from requests.auth import HTTPBasicAuth
import requests
from http.client import HTTPSConnection
from base64 import b64encode

cp= ConfigParser()
cp.read( r"jiraprop.ini" )

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')

cur = conn.cursor()

__user=cp.get('user details','user')
__apikey = cp.get('user details','apikey')
__server = cp.get('user details','server')
options = {'server': __server}
jira = JIRA(options, basic_auth=(__user,__apikey))
jql=cp.get('jql query','jql')
li=['issue','summary','assignee']
issues = jira.search_issues(jql)
keys=[]
for issue in issues:
    sql="insert into jiraconnector values("+f"'{issue}','{issue.fields.summary}','{issue.fields.assignee}','{issue.fields.issuetype}'"+")"
    
    cur.execute(sql)
    #keys.append(issue.key)
 
    #print(f"Issue id :{issue},summary:{issue.fields.summary},assignee :{issue.fields.assignee},issuetype:{issue.fields.issuetype}")

conn.commit()
print("jira gets connected and loaded with issues")    

print(keys)    

values=['issue']
dicts={}


dicts['issue']=keys
print(dicts)
'''
url='https://monsterprajju.atlassian.net/rest/api/2/project'
#apikey = '6wUUPpCr512aHu1tNr2595DF'
#head={'Accept':'application/json','Authorization':'Basic YWRtaW5Ac29mdGNyeWxpYy5jb206NndVVVBwQ3I1MTJhSHUxdE5yMkQ1OTVG'}
#userAndPass = b64encode(b"6wUUPpCr512aHu1tNr2D595F").decode("ascii")
head = { 'Accept':'application/json','Authorization' : 'access_token 6wUUPpCr512aHu1tNr2595DF'}
ret = requests.get(url,headers=head)
print(ret.status_code)
'''