url = 'http://182.0.0.111'
import requests
from time import sleep


def sending_post(user_id, user_data):
    if user_id.isdigit():
        for retryNumber in range(5):
            try:
                req = requests.post(f"{url}/{user_id}", data={"user_data": str(user_data)}, timeout=3)
                return(req.content)
            except requests.exceptions.Timeout:
                if retryNumber >= 5-1:
                    return(b'timeout')
                else:
                    sleep(1)
            except requests.ConnectionError:
                return(b'connection error')
            except:
                return(b'unspecified error')
    else:
        return(b'input not correct')


def client_write():
    user_id = input('user_id:')
    user_data = input('user_data:')
    content = sending_post(user_id, user_data)
    print(content.decode('ascii'))


if __name__ == "__main__":
    client_write()