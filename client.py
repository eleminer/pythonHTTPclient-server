import requests
import json

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

print("client software")
IdInput= input('ID:')
StringInput= input('Data or read-id:')
if RepresentsInt(IdInput):
    url = 'http://182.0.0.111:5000/'
    headers = {'Content-Type': 'application/json'}
    Data = {'userId': str(IdInput),
    'userData': str(StringInput),
    }
    try:
        req = requests.post(url, headers=headers, data=json.dumps(Data))
        if req.status_code==200:
            if str(req.content)=="b'File not found'":
                print("File not found")
            elif str(req.content)=="b'userId is not numeric'":
                print("UserId is not numeric")
            elif str(req.content)=="b''":
                pass
            else:
                content=str(req.text)
                print(content)
        else:
            print("something went wrong")
    except:
        print("server not reachable")
else:
    print("Input not correct")
