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

@app.route("/topDiningHalls")
def getTopDiningHalls():
    queryName = "topDiningHalls"
    return {queryName: []}

@app.route("/getUserHistory")
def getUserHistory():
    queryName = "getUserHistory"
    return {queryName: []}

@app.route("/getFoodReviews/:foodId")
def getFoodReviews():
    queryName = "foodReviews"
    return {queryName: []}

@app.route("/getDiningHallSignIns")
def getDiningHallSignIns():
    queryName = "diningHallSignIns"
    return {queryName: []}

@app.route("/")
def landingPage():
    queryName = "CULFA"
    return "CULFA"

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=3000)
