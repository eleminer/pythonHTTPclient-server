import requests

user_id = input('user_id:')
user_data = input('user_data:')
if user_id.isdigit():
    url = 'http://182.0.0.111/'
    try:
        req = requests.post(f"{url}{user_id}", headers={"user_data": str(user_data)})
        print(str(req.text))
    except:
        print("server not reachable")
else:
    print("input not correct")