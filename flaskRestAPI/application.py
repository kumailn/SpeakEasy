from flask import Flask, url_for
from flask import request

from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/xax')
def api_root():
    return 'Welcome'


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
