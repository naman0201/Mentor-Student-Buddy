import requests
import json


URL = "http://127.0.0.1:8000/api/register"
data = {
    'u_ID' : '0187CS191184',
    'email' : 'viveksingh0755@gmail.com',
    'name' : 'vivek singh',
    'password1' : '12345',
    'password2' : '12345',
    'usertype ' : 'Student'
}
json_data = json.dumps(data)
print("JsonData = ",json_data)
r = requests.post(url=URL,data = json_data)
data = r.json()

print(data)