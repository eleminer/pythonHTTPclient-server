from flask import Flask, request
app = Flask(__name__)
adminId=0
@app.route('/<id_user>')
def root_post_handle(id_user):
    userId = None
    userData = None

    if request.args.get("data")!=None:
        userData = request.args.get("data")
        userId = id_user
        print("ID:"+userId)
        print("String:"+userData)
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
    else:
        return 'parameter missing'

    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)

    