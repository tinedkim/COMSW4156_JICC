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
from werkzeug.wrappers import CommonRequestDescriptorsMixin
import database
<<<<<<< HEAD

=======
app = Flask(__name__)

import os
import random
import time
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)
>>>>>>> 4245be7e361f897cbf211040c8a8fadec5cf2657
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app = Flask(__name__, template_folder=tmpl_dir, static_folder=static_dir)


# login Page
@app.route('/login')
def login():
    return render_template("login.html")


# signup Page
@app.route('/signup')
def signup():
    return render_template("signup.html")


# create user
@app.route('/createuser', methods = ['POST'])
def create_user():
    name = request.form['name']
    uni = request.form['uni']
    email = request.form['email']
    print(name, uni, email)
    valid = database.createUser(name, uni, email)
    if valid == -1:
        return render_template("signup.html", valid = False)
    url = '/' + uni
    return redirect(url)


# check user credentials
@app.route('/checkCredentials', methods = ['POST'])
def checkCredentials():
    valid = -1
    name = request.form['name']
    email = request.form['email']
    valid = database.checkCredentials(name, email)
    if valid == -1:
        return render_template("login.html", valid = False)
    url = '/' + valid[0]['uni']
    return redirect(url)

'''
# user profile
@app.route('/<uni>')
def profile(uni):
    reviews = database.getUserReviews(uni)
    foodIDs = database.getUserReviewItemid(uni)
    return render_template("profile.html", uni = uni, reviews = reviews, foodIDs = foodIDs)

# add menu item review
@app.route('/<uni>/addReview', methods = ['POST'])
def addReview(uni):
    review = request.form['review']
    rating = request.form['rating']
    foodItem = request.form['foodItem']
    valid = -1
    valid = database.sendReview(uni, review, rating, foodItem)
    if valid == -1:
        return render_template("error.html")
    url = '/' + uni
    return redirect(url)
'''

# get dining hall menu items
@app.route('/getDiningMenu/<diningHall>')
<<<<<<< HEAD
def getDiningMenuItems(diningHall):
    return render_template("dininghall.html", menu = database.getDiningHallMenuItems(diningHall))

=======
def get_dining_menu_items(diningHall):
    items = database.get_dining_hall_menu_items(diningHall)
    return {"diningMenu":items} 
>>>>>>> 4245be7e361f897cbf211040c8a8fadec5cf2657

# get dining halls
@app.route('/getDiningHalls')
def get_dining_halls():
    return {"diningHalls": database.get_dining_halls()}
#Login Page
# @app.route('/login')
# def login():
#     return "<p>Login here</p>"

# #Signup Page
# @app.route('/signup')
# def signup():
#     return "<p>Sign up here</p>"

#check user credentials
# @app.route('/checkCredentials')
# def check_credentials():
#     queryName = "checkCredentials"
#     return {queryName: []}

#get top menu items
# @app.route("/topMenuItems")
# def get_top_menu_items():
#     queryName = "topMenuItems"
#     return {queryName: []}

#get top dining halls
# @app.route("/topDiningHalls")
# def get_top_dining_halls():
#     queryName = "topDiningHalls"
#     return {queryName: []}

#get user history
# @app.route("/getUserHistory")
# def get_user_history():
#     queryName = "getUserHistory"
#     return {queryName: []}

# get food items
@app.route('/getFoodItems')
def get_food_items():
    queryName = "getfoodItems"
    return {queryName: database.get_food_items()}


# get food reviews
@app.route("/getFoodReviews/<foodId>")
def getFoodReviews(foodId):
    return render_template("reviews.html", reviews = database.getReviewsForFoodItem(foodId), food = foodId)


# get dining hall swipes
@app.route("/getDiningHallSwipes/<diningHall>")
def get_dining_hall_swipes(diningHall):
    queryName = "diningHallSwipes"
    return {queryName: database.get_review_timestamps_for_dining_hall(diningHall)}

<<<<<<< HEAD
=======

>>>>>>> 4245be7e361f897cbf211040c8a8fadec5cf2657
# to implement later
'''
# get top menu items
@app.route("/topMenuItems")
def getTopMenuItems():
    queryName = "topMenuItems"
    return {queryName: database.getTopMenuItems()}

# get top dining halls
@app.route("/topDiningHalls")
def getTopDiningHalls():
    queryName = "topDiningHalls"
    return {queryName: []}

# get dining hall sign ins
@app.route("/getDiningHallSignIns")
def get_dining_hall_sign_ins():
    queryName = "diningHallSignIns"
    return {queryName: []}
'''

#home page
@app.route("/")
def landingPage():
<<<<<<< HEAD
    return render_template("landing.html", dininghalls = database.getDiningHalls())

=======
    return render_template("landing.html", dininghalls = database.get_dining_halls())
>>>>>>> 4245be7e361f897cbf211040c8a8fadec5cf2657

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
