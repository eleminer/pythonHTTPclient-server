import requests
from time import sleep
url = 'http://182.0.0.111'


def sending_get(file_number):
    if file_number.isdigit():
        for retryNumber in range(5):
            try:
                req = requests.get(f"{url}/{file_number}", timeout=3)
                return(str(req.content))
            except requests.exceptions.Timeout:
                if retryNumber >= 5-1:
                    return("timeout")
                else:
                    sleep(1)
            except requests.ConnectionError:
                return("connection error")
            except:
                return("unspecified error")
    else:
        return("input not correct")


def client_read():
    file_number = input('file number:')
    content = sending_get(file_number)
    print(content)


if __name__ == "__main__":
    client_read()
