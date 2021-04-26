import requests
from time import sleep

url = "http://127.0.0.1/"

def get_file_from_server(file_number):
    if file_number.isdigit():
        for retryNumber in range(5):
            try:
                req = requests.get(f"{url}/{file_number}", timeout=3)
                return req.content
            except requests.exceptions.Timeout:
                if retryNumber >= 5-1:
                    return b'timeout'
                else:
                    sleep(1)
            except requests.ConnectionError:
                return b'connection error'
            except:
                return b'unspecified error'
    else:
        return b'input not correct'


def client_read():
    file_number = input('file number:')
    content = get_file_from_server(file_number)
    print(content.decode('ascii'))


if __name__ == "__main__":
    client_read()
