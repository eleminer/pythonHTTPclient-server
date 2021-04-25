import requests
from time import sleep

user_id = input('user_id:')
user_data = input('user_data:')
if user_id.isdigit():
    url = 'http://182.0.0.111'
    for retryNumber in range(5):
        try:
            req = requests.post(f"{url}/{user_id}", data={"user_data": str(user_data)}, timeout=3)
            print(str(req.text))
            break
        except requests.exceptions.Timeout:
            print("timeout")
            if retryNumber >= 5-1:
                break
            else:
                print("try again...")
                sleep(1)
        except requests.ConnectionError:
            print("connection error")
            break
        except:
            print("unspecified error")
            break
else:
    print("input not correct")
