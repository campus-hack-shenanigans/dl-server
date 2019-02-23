"""Main file of the server implementation."""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/lyrics', methods=["POST"])
def postLyrics():
    words = request.form["words"]
    return words


if __name__ == '__main__':
    app.run()
