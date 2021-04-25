import requests
from time import sleep

file_number = input('file number:')
if file_number.isdigit():
    url = 'http://182.0.0.111'
    for retryNumber in range(5):
        try:
            req = requests.get(f"{url}/{file_number}", timeout=3)
            print(str(req.content))
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
