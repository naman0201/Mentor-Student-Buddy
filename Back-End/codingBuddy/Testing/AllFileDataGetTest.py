import requests
import json


URL = "http://127.0.0.1:8000/Buddyshare/APIBuddyView"

data = {
    'UserID':"160701"
}
json_data = json.dumps(data)
print("JsonData = ",json_data)
r = requests.post(url=URL,data = json_data)
print("r ==>>",r)
data = r.json()

print(data)