'''
Begin server at 3000 and expose endpoints
'''
import os

from sqlalchemy.sql.functions import user
import database
from flask import Flask, render_template, request, redirect, jsonify
from json import dumps
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from requests import get
from werkzeug.wrappers import CommonRequestDescriptorsMixin
from flask_wtf.csrf import CSRFProtect
from datetime import date, datetime

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app = Flask(__name__, template_folder=tmpl_dir, static_folder=static_dir)
app.config['SECRET_KEY'] = 'JICC' 


# csrf = CSRFProtect(app)
today = date.today()
now = datetime.now()


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
    valid = database.create_user(name, uni, email)
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
    valid = database.check_credentials(name, email)
    if valid == -1 or len(valid) == 0:
        return render_template("login.html", valid = False)
    url = '/' + valid[0]['uni']
    return redirect(url)


# user profile
@app.route('/<uni>')
def profile(uni):
    reviews = database.get_user_reviews(uni)
    foodIDs = database.get_user_review_item_id(uni)
    userreviews = []
    for review, id in zip(reviews, foodIDs):
        userreviews.append({**review, **id})
    return render_template("profile.html", uni = uni, userreviews = userreviews)


# add menu item review
@app.route('/<uni>/addReview', methods = ['GET', 'POST'])
def addReview(uni):
    if request.method == 'POST':
        review = request.form['review']
        rating = request.form['rating']
        foodItem = request.form['foodItem']
        date = today.strftime("%B %d, %Y")
        time = now.strftime("%H:%M:%S")
        datetime = date + " " + time
        valid = -1
        valid = database.send_review(uni, review, rating, foodItem, datetime)
        if valid == -1:
            return render_template("error.html")
        url = '/' + uni
        return redirect(url)
    else:
        foodItems = database.get_food_items()
        return render_template("addreview.html", uni = uni, foodItems = foodItems)


# get dining hall menu items
@app.route('/getDiningMenu/<diningHall>')
def get_dining_menu_items(diningHall):
    return render_template("dininghall.html", menu = database.get_dining_hall_menu_items(diningHall))


# get dining halls
@app.route('/getDiningHalls')
def get_dining_halls():
    return {"diningHalls": database.get_dining_halls()}


# get food items
@app.route('/getFoodItems')
def get_food_items():
    queryName = "getfoodItems"
    return {queryName: database.get_food_items()}


# get food reviews
@app.route("/getFoodReviews/<foodId>")
def getFoodReviews(foodId):
    return render_template("reviews.html", reviews = database.get_reviews_for_food_item(foodId), food = foodId)


# get dining hall swipes
@app.route("/getDiningHallSwipes/<diningHall>")
def get_dining_hall_swipes(diningHall):
    queryName = "diningHallSwipes"
    return {queryName: database.get_review_timestamps_for_dining_hall(diningHall)}


# get top menu items
@app.route("/topMenuItems")
def getTopMenuItems():
    queryName = "topMenuItems"
    return {queryName: database.get_top_menu_items()}


# get top dining halls
@app.route("/topDiningHalls")
def getTopDiningHalls():
    queryName = "topDiningHalls"
    return {queryName: database.get_top_dining_halls()}


# get dining hall sign ins
@app.route("/getDiningHallSignIns")
def get_dining_hall_sign_ins():
    queryName = "diningHallSignIns"
    return {queryName: database.get_dining_hall_sign_ins()}


#home page
@app.route("/")
def landingPage():
    dininghallstats = database.get_top_dining_halls()
    menuitemstats = database.get_top_menu_items()
    dailystats = database.get_daily_sign_ins()
    return render_template("landing.html", dininghalls = database.get_dining_halls(),
                           dininghallstats = dininghallstats, menuitemstats = menuitemstats,
                           dailystats=dailystats)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
