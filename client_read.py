url = 'http://182.0.0.111'
import requests
from time import sleep


def sending_get(file_number):
    if file_number.isdigit():
        for retryNumber in range(5):
            try:
                req = requests.get(f"{url}/{file_number}", timeout=3)
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


def client_read():
    file_number = input('file number:')
    content = sending_get(file_number)
    print(content.decode('ascii'))


if __name__ == "__main__":
    client_read()
