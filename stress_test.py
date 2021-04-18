import requests
from array import array
from random import randint
from time import sleep
import time
from multiprocessing import Process, Pool
from concurrent.futures import ThreadPoolExecutor
adminId=0

errorCount=0

def millis():
    return int(round(time.time() * 1000))

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
                    return ("error")
                elif str(req.content)=="b'userId is not numeric'":
                    print("UserId is not numeric")
                    return ("error")
                elif str(req.content)=="b'parameter missing'":
                    print("Parameter missing")
                    return ("error")
                elif str(req.content)=="b''":
                    pass
                else:
                    content=str(req.text)
                    print(content)
                    return str(req.content)
            else:
                print("something went wrong")
                return ("error")
        except:
            print("server not reachable")
            return ("error")
    else:
        print("Input not correct")
        return ("error")

def eachclient(clientID):
    start_time= millis()
    sleep(randint(1,10))
    for i in range(10):
        sending(str(clientID), str(i))
        print("ID:"+str(clientID)+"Data:"+str(i))
        sleep(1)
    print("ID:" + str(clientID) + " took " + str(millis() - start_time) + " ms")

def readingeachclientfile(clientID):
    global errorCount, adminId
    content=sending(str(adminId), str(clientID))
    print(content)
    if content ==str(b'0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'):
        print("pass")
    else:
        print("missing data")
        errorCount=errorCount+1

def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        ex.map(func, args)

def main():
    amountClients=5000
    clientNumber = list(range(1,amountClients+1))
    #pool = Pool(processes=amountClients)
    #pool.map(eachclient, clientNumber)
    multithreading(eachclient, clientNumber, 100)
    print("reading..... please wait")
    multithreading(readingeachclientfile, clientNumber, 100)
    if errorCount>0:
        print("failure... Number of errors: "+ str(errorCount))
    else: 
        print("success")



if __name__ == '__main__':
    main()