'''
Begin server at 3000 and expose endpoints
'''
import os
import random
import time

from flask import Flask, render_template, request, redirect, jsonify
from json import dumps
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from requests import get
import database
app = Flask(__name__)


# get dining hall menu items
@app.route('/getDiningMenu/<diningHall>')
def getDiningMenuItems(diningHall):
    queryName = "diningMenu"
    return {queryName: database.getDiningHallMenuItems(diningHall)}


# get dining halls
@app.route('/getDiningHalls')
def getDiningHalls():
    queryName = "diningHalls"
    return {queryName: database.getDiningHalls()}


# get food items
@app.route('/getFoodItems')
def getFoodItems():
    queryName = "getfoodItems"
    return {queryName: database.getFoodItems()}


# get food reviews
@app.route("/getFoodReviews/<foodId>")
def getFoodReviews(foodId):
    queryName = "foodReviews"
    return {queryName: database.getReviewsForFoodItem(foodId)}


# get dining hall swipes
@app.route("/getDiningHallSwipes/<diningHall>")
def getDiningHallSwipes(diningHall):
    queryName = "diningHallSwipes"
    return {queryName: database.getReviewTimestampsForDiningHall(diningHall)}


#home page
@app.route("/")
def landingPage():
    queryName = "CULFA"
    return render_template("landing.html")

# Login Page
@app.route('/login')
def login():
    return render_template("login.html")

# Signup Page
@app.route('/signup')
def signup():
    return render_template("signup.html")


# to implement later

'''
@app.route('/<custID>/profile')
def profile():
    pass

@app.route('/<custID>/profile/add', methods = ['POST'])
def addReview(custID):
    review = request.form['review']
    diningHall = request.form['diningHall']
    menuItem = request.form['menuItem']
    url = '/' + custID + '/profile'
    database.sendReview(custID, review, diningHall, menuItem)
    return url


@app.route('/createuser', methods = ['POST'])
def createUser():
    name = request.form['name']
    email = request.form['email']
    custID = database.createCustomer(name, email)
    url = '/' + str(custID)
    return url


# check user credentials
@app.route('/checkCredentials')
def checkCredentials():
    queryName = "checkCredentials"
    return {queryName: []}

# get top menu items
@app.route("/topMenuItems")
def getTopMenuItems():
    queryName = "topMenuItems"
    return {queryName: []}

# get top dining halls
@app.route("/topDiningHalls")
def getTopDiningHalls():
    queryName = "topDiningHalls"
    return {queryName: []}

# get user history
@app.route("/getUserHistory")
def getUserHistory():
    queryName = "getUserHistory"
    return {queryName: []}

# get dining hall sign ins
@app.route("/getDiningHallSignIns")
def getDiningHallSignIns():
    queryName = "diningHallSignIns"
    return {queryName: []}
'''

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=3000)
