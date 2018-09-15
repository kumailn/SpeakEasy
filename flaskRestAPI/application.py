from flask import Flask, url_for
from flask import request

app = Flask(__name__)

# test route


@app.route('/xax')
def api_root():
    return 'Welcome'

# POST method
# uses flask request to obtain the file that was POSTed with the audience_image tag


@app.route('/messages', methods=['POST'])
def api_messages():
    if 'audience_image' in request.files:
        f = request.files['audience_image']
        f.save("test"+f.filename)
        return "file uploaded"

    else:
        return "Error has occured"


if __name__ == '__main__':
    app.run()
