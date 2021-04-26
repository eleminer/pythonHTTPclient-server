from time import sleep
from concurrent.futures import ThreadPoolExecutor
from random import randint
from client_read import get_file_from_server
from client_write import post_text_to_server

error_count_reading = 0

url = "http://127.0.0.1/"

def multithreading(func, args, workersCount):
    with ThreadPoolExecutor(workersCount) as ex:
        ex.map(func, args)


def write_data(user_id):
    sleep(randint(1, 10))
    for i in range(10):
        post_text_to_server(str(user_id), str(i))
        print(f"ID:{user_id}Data:{str(i)}")
        sleep(1)


def read_data(user_id):
    global error_count_reading
    content = get_file_from_server(str(user_id))
    print(str(content))
    if str(content) == str(b'0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'):
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
