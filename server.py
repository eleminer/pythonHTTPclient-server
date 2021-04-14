from flask import Flask, request, Response
app = Flask(__name__)
adminId=2
@app.route('/', methods=['POST'])
def main():
    request_data = request.get_json()
    userId = None
    userData = None

    if request_data:
        if 'userId' in request_data:
            userId = request_data['userId']
            print("userID:"+userId)
        if 'userData' in request_data:
            userData = request_data['userData']
            print("userData:"+userData)
        if userId!=None and userData!=None:
            if userId.isnumeric()==True:
                if int(userId)==adminId:
                    try:
                        fn=open(userData+".txt","U")
                        return fn.read()
                    except IOError: 
                        print ("Error: File does not appear to exist.")
                        return 'File not found'
                else:
                    f = open(userId+".txt", "a")
                    f.write(userData+"\n")
                    f.close()
    return 'I have no more data for you'