import requests
from array import array
from random import randint
from time import sleep

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def sending(IdInput,StringInput):
    if RepresentsInt(IdInput):
        url = 'http://182.0.0.111/'
        payload = {'data': StringInput}
        try:
            req = requests.get(url+IdInput,params=payload)
            if req.status_code==200:
                if str(req.content)=="b'File not found'":
                    print("File not found")
                elif str(req.content)=="b'userId is not numeric'":
                    print("UserId is not numeric")
                elif str(req.content)=="b'parameter missing'":
                    print("Parameter missing")
                elif str(req.content)=="b''":
                    pass
                else:
                    content=str(req.text)
                    print(content)
            else:
                print("something went wrong")
        except:
            print("server not reachable")
    else:
        print("Input not correct")

def eachclient(clientID):
    sleep(randint(1,10))
    for i in range(10):
        sending(str(clientID), str(i))
        print("ID:"+str(clientID)+"Data:"+str(i))
        sleep(3)

def main():
    arr_messagenumber = [0] * 1000
    for number in range(len(arr_messagenumber)):
        eachclient(number+1)


if __name__ == '__main__':
    main()