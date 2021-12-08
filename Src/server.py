'''
Begin server at 3000 and expose endpoints
'''

from flask import Flask, render_template, request, redirect, jsonify
from json import dumps
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from requests import get
import database
app = Flask(__name__)

import os
import random
import time
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

#get dining hall menu items
@app.route('/getDiningMenu/<diningHall>')
def get_dining_menu_items(diningHall):
    items = database.get_dining_hall_menu_items(diningHall)
    return {"diningMenu":items} 

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

@app.route('/getFoodItems')
def get_food_items():
    queryName = "getfoodItems"
    return {queryName: database.get_food_items()}

#get food reviews
@app.route("/getFoodReviews/<foodId>")
def get_food_reviews(foodId):
    queryName = "foodReviews"
    return {queryName: database.get_reviews_for_food_item(foodId)}

@app.route("/getDiningHallSwipes/<diningHall>")
def get_dining_hall_swipes(diningHall):
    queryName = "diningHallSwipes"
    return {queryName: database.get_review_timestamps_for_dining_hall(diningHall)}

@app.route("/getDiningHallSignIns")
def get_dining_hall_sign_ins():
    queryName = "diningHallSignIns"
    return {queryName: []}

#home page
@app.route("/")
def landing_page():
    queryName = "CULFA"
    return "CULFA"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
