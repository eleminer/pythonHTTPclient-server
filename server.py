from flask import Flask, request
app = Flask(__name__)

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

    return ''