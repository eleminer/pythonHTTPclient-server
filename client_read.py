import requests

StringInput = input('file number:')
if RepresentsInt(IdInput):
    url = 'http://182.0.0.111/'
    payload = {'data': StringInput}
    try:
        req = requests.get(url+IdInput, params=payload)
        if req.status_code == 200:
            if str(req.content) == "b'File not found'":
                print("File not found")
            elif str(req.content) == "b'userId is not numeric'":
                print("UserId is not numeric")
            elif str(req.content) == "b'parameter missing'":
                print("Parameter missing")
            elif str(req.content) == "b''":
                pass
            else:
                content = str(req.text)
                print(content)
        else:
            print("something went wrong")
    except:
        print("server not reachable")
else:
    print("Input not correct")
