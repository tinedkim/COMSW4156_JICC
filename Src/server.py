'''
Begin server at 3000 and expose endpoints
'''

from flask import Flask
import sys
import database

app = Flask(__name__)


@app.route("/topMenuItems")
def getTopMenuItems():
    queryName = "topMenuItems"
    return {queryName: []}

@app.route("/")
def landingPage():
    queryName = "CULFA"
    return "CULFA"

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=3000)
