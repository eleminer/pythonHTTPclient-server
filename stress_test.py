from time import sleep
from multiprocessing import Process, Pool
from concurrent.futures import ThreadPoolExecutor
import requests
from array import array
from random import randint
error_count_reading = 0
url = 'http://182.0.0.111'


def sending_post(user_id, user_data):
    if user_id.isdigit():
        for retryNumber in range(5):
            try:
                req = requests.post(f"{url}/{user_id}", data={"user_data": str(user_data)}, timeout=3)
                print(str(req.text))
                break
            except requests.exceptions.Timeout:
                print("timeout")
                if retryNumber >= 5-1:
                    print("timeout")
                    break
                else:
                    print("timeout, try again...")
                    sleep(1)
            except requests.ConnectionError:
                print("connection error")
                break
            except:
                print("unspecified error")
                break
    else:
        print("input not correct")


def sending_get(file_number):
    if file_number.isdigit():
        for retryNumber in range(5):
            try:
                req = requests.get(f"{url}/{file_number}", timeout=3)
                return str(req.content)
            except requests.exceptions.Timeout:
                print("timeout")
                if retryNumber >= 5-1:
                    return("timeout")
                else:
                    print("try again...")
                    sleep(1)
            except requests.ConnectionError:
                return("connection error")
            except:
                return("unspecified error")
    else:
        return("input not correct")


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        ex.map(func, args)


def write_data(user_id):
    sleep(randint(1, 10))
    for i in range(10):
        sending_post(str(user_id), str(i))
        print(f"ID:{user_id}Data:{str(i)}")
        sleep(1)


def read_data(user_id):
    global error_count_reading
    content = sending_get(str(user_id))
    print(content)
    if content == str(b'0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'):
        print("pass")
    else:
        print("missing data")
        error_count_reading += 1


def main():
    amountClients = 5000
    user_id = list(range(1, amountClients+1))
    #pool = Pool(processes=amountClients)
    #pool.map(eachclient, user_id)
    multithreading(write_data, user_id, 100)
    multithreading(read_data, user_id, 100)
    if error_count_reading == 0:
        print("test successful")
    else:
        print(f"something went wrong: {error_count_reading} files not match the expectation")


if __name__ == '__main__':
    main()
