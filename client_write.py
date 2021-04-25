import requests
from time import sleep
url = 'http://182.0.0.111'


def sending_post(user_id, user_data):
    if user_id.isdigit():
        for retryNumber in range(5):
            try:
                req = requests.post(f"{url}/{user_id}", data={"user_data": str(user_data)}, timeout=3)
                print(req.text)
                return(str(req.text))
            except requests.exceptions.Timeout:
                print("timeout")
                if retryNumber >= 5-1:
                    return("timeout")
                else:
                    print("timeout, try again...")
                    sleep(1)
            except requests.ConnectionError:
                print("connection error")
                return("connection error")
            except:
                print("unspecified error")
                return("unspecified error")
    else:
        print("input not correct")


def client_write():
    user_id = input('user_id:')
    user_data = input('user_data:')
    sending_post(user_id, user_data)

    
if __name__ == "__main__":
    client_write()