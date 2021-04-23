from flask import Flask, request
app = Flask(__name__)

@app.route('/<id_user>', methods=['GET'])
def root_post_handle(id_user):
    if request.args.get("data") != None:
        userData = request.args.get("data")
        print(userData)
    else:
        return 'parameter missing'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)
