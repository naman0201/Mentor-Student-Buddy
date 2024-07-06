import requests
import json


URL = "http://127.0.0.1:8000/api/contact"
data = {
    'email':'rrr160701@gmail.com',
    'name':'Ritik ',
    'contactno':'8085627897',
    'query':'This is an Qury for DBA to solve'
}
json_data = json.dumps(data)
print("JsonData = ",json_data)
r = requests.post(url=URL,data = json_data)
data = r.json()

print(data)