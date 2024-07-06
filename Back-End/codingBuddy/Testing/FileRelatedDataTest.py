import requests
import json


URL = "http://127.0.0.1:8000/Buddyshare/FileRelatedInfoSave"
headers = {'content-type': 'application/json'}
data = {
    'UserID' : '2',
    'tobeDelete': 'False', 
    'ShareWithEveryOne': 'False', 
    'toShareWith': '220' 
}
# 2022-09-07 01:16
# 'TimeForDeletion': '2022-09-12T18:43:23.167207Z', 
    
    
    # 'DateName':'2023-08-22',
    # 'TimeName':'01:02:12',

 

json_data = json.dumps(data)
print("JsonData = ",json_data)
r = requests.post(url=URL,data = json_data, headers=headers)
data = r.json()

print(data)

# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# headers = {'content-type': 'application/json'}

# r = requests.post(url, data=json.dumps(payload), headers=headers)