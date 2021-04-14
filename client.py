import requests
import json


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

print("Client Software")
IdInput= raw_input('ID:')
StringInput= raw_input('Data:')
if RepresentsInt(IdInput):
    url = 'http://182.0.0.111:5000/'
    headers = {'Content-Type': 'application/json'}
    Data = {'userId': str(IdInput),
    'userData': str(StringInput),
    }
    req = requests.post(url, headers=headers, data=json.dumps(Data))
    print(req.status_code)
else:
    print("Eingabe nicht korrekt")
