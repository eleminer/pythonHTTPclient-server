import requests

file_number = input('file number:')
if file_number.isdigit():
    url = 'http://182.0.0.111/'
    try:
        req = requests.get(f"{url}/{file_number}") 
        print(str(req.text))
    except:
        print("server not reachable")
else:
    print("input not correct")