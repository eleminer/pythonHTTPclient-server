import requests
from time import sleep

url = "http://127.0.0.1/"

def post_text_to_server(user_id, user_data):
    if user_id.isdigit():
        for retryNumber in range(5):
            try:
                req = requests.post(f"{url}/{user_id}", data={"user_data": str(user_data)}, timeout=3)
                return req.content
            except requests.exceptions.Timeout:
                sleep(1)
            except requests.ConnectionError:
                return b'connection error'
            except:
                return b'unspecified error'

            return b'timeout'
    else:
        return b'input not correct'


def client_write():
    user_id = input('user_id:')
    user_data = input('log message:')
    content = post_text_to_server(user_id, user_data)
    print(content.decode('ascii'))


if __name__ == "__main__":
    client_write()