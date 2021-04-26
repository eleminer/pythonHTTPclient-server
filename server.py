from flask import Flask, request, make_response
from time import sleep
app = Flask(__name__)


@app.route('/<file_number>', methods=['GET'])
def root_get_handle(file_number):
    if file_number.isdigit():
        try:
            with open(f"./logData/{file_number}.txt", "r") as f:
                response = make_response(f.read(), 200)
            response.mimetype = "text/plain"
            return response
        except IOError:
            return 'log not found!', 404
    else:
        return 'bad request!', 400


@app.route('/<user_id>', methods=['POST'])
def root_post_handle(user_id):
    user_data = request.form.get('user_data')
    print(str(user_data))
    if user_data is not None and user_id.isdigit():
        for retryNumber in range(10):
            try:
                with open(f"./logData/{user_id}.txt", "a") as f:
                    f.write(f"{user_data}\n")
                return 'success'
            except IOError:
                sleep(0.10)
        return 'service unavailable', 503
    else:
        return 'bad request', 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)
