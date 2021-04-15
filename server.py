from flask import Flask, request, Response
app = Flask(__name__)
adminId=2
@app.route('/', methods=['POST'])
def root_post_handle():
    request_data = request.get_json()
    userId = None
    userData = None

    if request_data:
        if 'userId' in request_data:
            userId = request_data['userId']
        if 'userData' in request_data:
            userData = request_data['userData']
        if userId!=None and userData!=None:
            if userId.isnumeric()==True:
                if int(userId)==adminId:
                    try:
                        with open(userData+".txt","r") as fn:
                            return fn.read()
                    except IOError: 
                        return 'File not found'
                else:
                    with open(userId+".txt", "a") as f:
                        f.write(f"{userData}\n")
            else:
                return 'userId is not numeric'
    return ''