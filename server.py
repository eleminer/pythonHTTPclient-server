from flask import Flask, request, render_template
from time import sleep
app = Flask(__name__)


@app.route('/<file_number>', methods=['GET'])
def root_get_handle(file_number):
    if file_number.isdigit():
        try:
            with open(f"{file_number}.txt", "r") as f:
                return f.read()
        except IOError:
            return 'file not found!', 400
    else:
        return 'bad request!', 400


@app.route('/<user_id>', methods=['POST'])
def root_post_handle(user_id):
    user_data = request.headers.get('user_data')
    if user_data is not None and user_id.isdigit():
        count = 0
        maxTries = 3
        while True:
            try:
                with open(f"{user_id}.txt", "a") as f:
                    f.write(f"{user_data}\n")
                return 'success'
            except IOError:
                if count >= maxTries:
                    return 'service unavailable', 503
                else:
                    count += 1
                    sleep(2)
    else:
        return 'bad request', 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)
