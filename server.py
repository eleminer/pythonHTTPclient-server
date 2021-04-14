from flask import Flask, request
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
                if int(userId)==adminId and userData=="recieve":
                    print("recieveMode")
                    
                else:
                    print("writeMode")
                    f = open(userId+".txt", "a")
                    f.write(userData+"\n")
                    f.close()

    return ''