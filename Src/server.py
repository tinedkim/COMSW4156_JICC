'''
Begin server at 3000 and expose endpoints
'''

from flask import Flask
import sys


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=3000)
