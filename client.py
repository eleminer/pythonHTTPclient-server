import requests

url = 'http://182.0.0.111:5000/'
headers = {'Content-Type': 'application/json'}
body = """{
    "userData" : "1recieve",
    "userId" : "2"
}"""

req = requests.post(url, headers=headers, data=body)

print(req.status_code)